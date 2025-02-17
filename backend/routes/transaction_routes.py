from flask import Blueprint, request, jsonify
from services.transaction_service import TransactionAggregator

transaction_bp = Blueprint("transaction_bp", __name__, url_prefix="/")

@transaction_bp.route("/aggregate", methods=["GET"])
def aggregate():
    group_by = request.args.get("group_by")
    if not group_by:
        return jsonify({"error": "group_by parameter is required"}), 400

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    customer_id = request.args.get("customer_id")
    item_id = request.args.get("item_id")

    # Only create filters dict if at least one filter is provided
    filters = {}
    if customer_id:
        filters["customer_id"] = int(customer_id)
    if item_id:
        filters["item_id"] = int(item_id)
    if start_date and end_date:
        filters["date_range"] = {"start": start_date, "end": end_date}

    # If no filters were added, pass None instead of empty dict
    filters = filters if filters else None

    if group_by == "date_range" and (not start_date or not end_date):
        return jsonify({"error": "Start and end dates are required for date range aggregation."}), 400

    try:
        aggregation_result, status_code = TransactionAggregator.aggregate_transactions(group_by, filters)
        return jsonify(aggregation_result), status_code

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
