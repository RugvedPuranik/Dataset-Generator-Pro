from flask import Flask, render_template, request, send_file
from generator import generate_dataset, make_dirty
import os

app = Flask(__name__)

GENERATED_FOLDER = "generated"

if not os.path.exists(GENERATED_FOLDER):
    os.makedirs(GENERATED_FOLDER)

stats = {
    "datasets_generated": 0,
    "rows_generated": 0,
    "last_dataset": "None"
}

AVAILABLE_COLUMNS = [
    "Order ID",
    "Order Date",
    "Ship Date",
    "Customer ID",
    "Customer Name",
    "Customer Segment",
    "Product ID",
    "Product Name",
    "Category",
    "State",
    "City",
    "Pincode",
    "Quantity",
    "Unit Price",
    "Discount(%)",
    "Sales Amount",
    "Cost Price",
    "Profit",
    "Payment Mode",
    "Delivery Status",
    "Supplier Name",
    "Supplier Email",
    "Stock Left",
    "Auto Reorder",
    "Reorder Quantity"
]

ALL_COLUMNS = [
    "Order ID",
    "Order Date",
    "Ship Date",
    "Customer ID",
    "Customer Name",
    "Customer Segment",
    "Product ID",
    "Product Name",
    "Category",
    "State",
    "City",
    "Pincode",
    "Quantity",
    "Unit Price",
    "Discount(%)",
    "Sales Amount",
    "Cost Price",
    "Profit",
    "Payment Mode",
    "Delivery Status",
    "Supplier Name",
    "Supplier Email",
    "Stock Left",
    "Auto Reorder",
    "Reorder Quantity"
]


@app.route("/")
def home():

    return render_template(
        "index.html",
        stats=stats,
        preview=None,
        columns=ALL_COLUMNS
    )


@app.route("/generate", methods=["POST"])
def generate():

    dataset_name = request.form["dataset_name"]

    num_rows = int(
        request.form["num_rows"]
    )

    output_format = request.form["output_format"]

    selected_columns = request.form.getlist("columns")

    dataset_type = request.form.get(
        "dataset_type",
        "clean"
    )

    error_percentage = int(
        request.form.get(
            "error_percentage",
            10
        )
    )

    clean_df = generate_dataset(
        dataset_name,
        num_rows,
        output_format,
        selected_columns
    )

    df = clean_df.copy()

    if dataset_type == "dirty":

        df = make_dirty(
            df,
            error_percentage
        )

    filename = f"{dataset_name}.{output_format}"

    solution_filename = None

    if dataset_type == "dirty":

        solution_filename = (
            f"{dataset_name}_CLEAN_SOLUTION.{output_format}"
        )

        solution_path = os.path.join(
            GENERATED_FOLDER,
            solution_filename
        )

        if output_format == "csv":
            clean_df.to_csv(
                solution_path,
                index=False
            )

        else:
            clean_df.to_excel(
                solution_path,
                index=False
            )

    filepath = os.path.join(
        GENERATED_FOLDER,
        filename
    )

    if output_format == "csv":
        df.to_csv(filepath, index=False)

    else:
        df.to_excel(filepath, index=False)

    stats["datasets_generated"] += 1
    stats["rows_generated"] += num_rows
    stats["last_dataset"] = dataset_name

    preview = (
        df.head(10)
        .to_html(
            classes="table",
            index=False
        )
    )

    return render_template(
        "index.html",
        stats=stats,
        preview=preview,
        download_file=filename,
        solution_file=solution_filename,
        columns=ALL_COLUMNS
    )


@app.route("/download/<filename>")
def download(filename):

    path = os.path.join(
        GENERATED_FOLDER,
        filename
    )

    return send_file(
        path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)