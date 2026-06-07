import pandas as pd
import random
from datetime import datetime, timedelta

products_df = pd.read_csv("data/product_categories.csv")
products_df = products_df.dropna(subset=["Category", "Product"])
locations_df = pd.read_csv("data/india_real_state_city_pincode_754_locations.csv")

products_df["Product ID"] = [
    f"PROD{1000+i}"
    for i in range(len(products_df))
]

# regions=["North","South","East","West"]

payment_modes=["Cash","Credit Card","UPI","Net Banking"]

Delivery_status=["Delivered","Pending","Returned","Cancelled"]

Customer_segments=["Consumer","Corporate","Home office"]

First_name = {
    "Male": [
        "Aarav","Vivaan","Aditya","Arjun","Krishna",
        "Rohan","Rahul","Karan","Varun","Aakash",
        "Aniket","Siddharth","Harsh","Yash","Atharva",
        "Omkar","Pranav","Saurabh","Shubham","Akshay",
        "Abhishek","Nikhil","Ritesh","Sameer","Vishal",
        "Ruturaj","Tushar","Jay","Parth","Dhruv",
        "Ishaan","Vedant","Aryan","Raghav","Manav",
        "Rudra","Tanmay","Chirag","Deepak","Mayur",
        "Nitin","Tejas","Swapnil","Sanket","Ansh",
        "Mihir","Gaurav","Piyush","Kunal","Aman"
    ],

    "Female": [
        "Aadhya","Ananya","Diya","Kavya","Saanvi",
        "Ira","Myra","Riya","Sneha","Priya",
        "Pooja","Neha","Shruti","Aarti","Vaishnavi",
        "Rutuja","Sakshi","Komal","Mansi","Prachi",
        "Tejal","Anushka","Meera","Nisha","Khushi",
        "Aisha","Pari","Tanvi","Swara","Trisha",
        "Ishita","Riddhi","Anjali","Pallavi","Shweta",
        "Bhavna","Vidhi","Muskan","Simran","Payal",
        "Rashmi","Nandini","Divya","Harini","Janhavi",
        "Shraddha","Avni","Nikita","Mahima","Reva"
    ]
}

Middle_name = [
    "Anand","Ashok","Balaji","Bhaskar","Chandra",
    "Dattatray","Devendra","Ganesh","Gopal","Govind",
    "Hari","Hemant","Jagannath","Jitendra","Kailash",
    "Keshav","Mahadev","Madhav","Manohar","Mukesh",
    "Narayan","Nitin","Prakash","Rajendra","Ramesh",
    "Ravindra","Sachin","Sanjay","Santosh","Sharad",
    "Shankar","Shivaji","Shrikant","Subhash","Suresh",
    "Uday","Vasant","Vijay","Vinay","Vishnu",
    "Yogesh","Pramod","Sunil","Dilip","Milind",
    "Pravin","Sudhir","Ajit","Arvind","Bharat",
]

Last_name = [
    "Patil","Sharma","Verma","Gupta","Joshi",
    "Kulkarni","Deshmukh","Pawar","Jadhav","Shinde",
    "More","Chavan","Patankar","Sawant","Naik",
    "Rane","Salunkhe","Gaikwad","Bhosale","Kadam",
    "Kale","Mane","Thakur","Tiwari","Mishra",
    "Pandey","Dubey","Yadav","Singh","Chauhan",
    "Rathod","Rajput","Kapoor","Malhotra","Khanna",
    "Mehta","Shah","Bhatt","Trivedi","Pandya",
    "Desai","Patel","Agarwal","Bajaj","Arora",
    "Saxena","Bhatia","Goyal","Mittal","Soni",
    "Nair","Menon","Pillai","Iyer","Iyengar",
    "Reddy","Rao","Naidu","Murthy","Shetty",
    "Hegde","Kamath","Pai","Acharya","Prabhu",
    "Fernandes","D'Souza","Pinto","Lobo","Mascarenhas",
    "Banerjee","Mukherjee","Chatterjee","Bose","Ghosh",
    "Das","Sen","Dutta","Roy","Sarkar",
    "Mahajan","Wagh","Puranik","Apte","Godbole",
    "Lele","Limaye","Phadke","Agashe","Paranjape",
    "Ranade","Kanetkar","Dixit","Date","Karandikar",
    "Bhave","Oak","Nene","Thatte","Bapat"
]

Suppliers = [
    "Apex Solutions",
    "Vertex Enterprises",
    "Prime Associates",
    "BlueSky Ventures",
    "Elite Corporation",
    "Summit Traders",
    "Pioneer Industries",
    "Infinity Services",
    "NextGen Solutions",
    "Global Enterprises",

    "SilverLine Associates",
    "BrightPath Solutions",
    "GoldenPeak Industries",
    "RapidEdge Ventures",
    "CoreLink Services",
    "SmartBridge Technologies",
    "Visionary Enterprises",
    "Quantum Solutions",
    "Unity Traders",
    "FutureWave Industries",

    "Starline Corporation",
    "Dynamic Associates",
    "RoyalEdge Enterprises",
    "SkyHigh Solutions",
    "TrustPoint Services",
    "BrightFuture Ventures",
    "MetroLink Industries",
    "Evergreen Associates",
    "TrueNorth Enterprises",
    "Nimbus Solutions",

    "CrystalWave Corporation",
    "Velocity Ventures",
    "Optimum Enterprises",
    "GreenLeaf Industries",
    "Grand Horizon Services",
    "Pinnacle Associates",
    "UrbanCore Solutions",
    "Axis Enterprises",
    "BridgePoint Industries",
    "Titan Ventures",

    "NovaEdge Solutions",
    "Harmony Enterprises",
    "Excel Corporation",
    "Crown Associates",
    "Beacon Industries",
    "Elevate Ventures",
    "ProActive Services",
    "NorthStar Enterprises",
    "AlphaBridge Solutions",
    "Zenith Corporation",

    "Aurora Enterprises",
    "Orbit Solutions",
    "BluePeak Industries",
    "Matrix Associates",
    "Fusion Ventures",
    "BrightStone Services",
    "Vertex Global",
    "Astra Enterprises",
    "Momentum Industries",
    "Prestige Solutions",

    "Horizon Corporation",
    "Sigma Associates",
    "Nexus Enterprises",
    "GrowthPoint Ventures",
    "PeakLine Industries",
    "Velocity Global",
    "FirstChoice Solutions",
    "EliteEdge Associates",
    "Infinity Ventures",
    "SmartCore Enterprises",

    "VisionPoint Industries",
    "GoldenBridge Services",
    "CapitalEdge Corporation",
    "BlueOrbit Solutions",
    "Dynamic Ventures",
    "SummitPoint Enterprises",
    "PrimeAxis Industries",
    "TrueValue Associates",
    "NextStep Solutions",
    "EverBright Corporation",

    "UrbanPeak Ventures",
    "CrystalEdge Enterprises",
    "TitanCore Industries",
    "ApexBridge Solutions",
    "Pioneer Global",
    "UnityPoint Associates",
    "MetroWave Ventures",
    "NovaBridge Enterprises",
    "Skyline Industries",
    "QuantumEdge Solutions",

    "CrestPoint Corporation",
    "FutureCore Enterprises",
    "AlphaWave Industries",
    "BrightAxis Solutions",
    "ElitePoint Ventures",
    "StarBridge Associates",
    "VertexLine Enterprises",
    "GrandPeak Industries",
    "SmartWave Solutions",
    "NorthBridge Corporation"
]

Price_Range = {
    "Electronics": (5000, 100000),
    "Furniture": (1000, 50000),
    "Office Supplies": (10, 1000),
    "Grocery": (20, 5000),
    "Books": (100, 3000),
    "Medical Supplies": (50, 20000),
    "Sports Equipment": (100, 30000),
    "Clothing": (200, 10000),
    "Footwear": (300, 15000),
    "Kitchen Appliances": (500, 50000)
}

domains = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "hotmail.com",
    "rediffmail.com",
    "business.in",
    "enterprise.in",
    "corp.in",
    "solutions.in",
    "group.in"
]

email_prefixes = [
    "info",
    "sales",
    "support",
    "contact",
    "admin",
    "service",
    "accounts",
    "helpdesk",
    "office",
    "care"
]


def generate_dataset(dataset_name,num_rows,output_format,selected_columns=None):
    records = []
    start_date = datetime.now() - timedelta(days=730)

    for i in range(num_rows):
        # Order ID generator
        order_id=f"ORD{1000+i}"
        
        
        # Order Date generator
        order_date = (
            start_date +
            timedelta(days=random.randint(0,730))
        ).date()
        
        
        # Shipping Date Generator
        ship_date = order_date + timedelta(
            days=random.randint(1,7)
        )
        
        
        # Gender Genrator 
        gender = random.choice(["Male", "Female"])

        
        # Name Generator
        first_name = random.choice(First_name[gender])
        middle_name = random.choice(Middle_name)
        last_name = random.choice(Last_name)


        # Customer Name generator
        customer_name = f"{first_name} {middle_name} {last_name}"     
        
        
        # Customer ID generator                             
        # customer_id = f"CUST{random.randint(100,999)}" # If the dataset needs duplicate customers
        # customer_id = f"CUST{random.randint(10000,99999)}"

        # Customer ID generator (If more unique customers are needed)
        customer_id = f"CUST{i+1000}"
        
        # Customer Segment generator
        customer_segment=random.choice(Customer_segments)


        # Product category and product generator
        product_row = products_df.sample(1).iloc[0]

        category = product_row["Category"]
        product_name = product_row["Product"]
        
        # Product ID generator
        product_id = product_row["Product ID"]


        # Location generator
        location_row = locations_df.sample(1).iloc[0]

        state = location_row["State"]
        city = location_row["City"]
        pincode = location_row["Pincode"]


        # order quantity generator
        quantity=random.randint(1,10)


        # Product Price, Sale amount and profit generator
        min_price, max_price = Price_Range[category]
        unit_price = random.randint(min_price, max_price)
        discount=random.choice([0,5,10,15,20])

        sales_amount = round(
            quantity * unit_price * (1 - discount / 100),
            2
        )

        cost_price = round(
            sales_amount * random.uniform(0.6, 0.9),
            2
        )

        profit = round(
            sales_amount - cost_price,
            2
        )

        stock_left=random.randint(0,50)
        if stock_left<10:
            auto_reorder="Yes"
            reorder_quantity=random.randint(20,50)
        else:
            auto_reorder="No"
            reorder_quantity=0


        #  Supplier name generator.
        supplier_name = random.choice(Suppliers)
        
        
        # Supplier Email generator
        if random.random() < 0.5:

            supplier_email = (
                random.choice(email_prefixes)
                + "@"
                + supplier_name.lower().replace(" ", "")
                + ".com"
            )

        else:

            supplier_email = (
                supplier_name.lower().replace(" ", "")
                + "@"
                + random.choice(domains)
            )
        
        
        # Payment mode generator
        payment_mode = random.choice(payment_modes)
        
        
        # Delivery status generator
        delivery=random.choice(Delivery_status)

        records.append({

            "Order ID":order_id,
            "Order Date":order_date,
            "Ship Date": ship_date,
            "Customer ID":customer_id,
            "Customer Name": customer_name,
            "Customer Segment": customer_segment,
            "Product ID": product_id,
            "Product Name":product_name,
            "Category":category,
            "State":state,
            "City":city,
            "Pincode":pincode,
            "Quantity":quantity,
            "Unit Price":unit_price,
            "Discount(%)":discount,
            "Sales Amount":round(sales_amount,2),
            "Cost Price":round(cost_price,2),
            "Profit":round(profit,2),
            "Payment Mode":payment_mode,
            "Delivery Status":delivery,
            "Supplier Name":supplier_name,
            "Supplier Email":supplier_email,
            "Stock Left":stock_left,
            "Auto Reorder":auto_reorder,
            "Reorder Quantity":reorder_quantity
        })

    df = pd.DataFrame(records)

    # If user selected specific columns
    if selected_columns:

        valid_columns = [
            col
            for col in selected_columns
            if col in df.columns
        ]

        df = df[valid_columns]

    return df

def make_dirty(df, error_percentage):

    dirty_df = df.copy()

    rows_to_modify = max(
        1,
        int(len(dirty_df) * error_percentage / 100)
    )

    errors_per_type = max(
        1,
        rows_to_modify // 6
    )

    # --------------------------
    # Missing Values
    # --------------------------

    for _ in range(errors_per_type):

        row = random.randint(
            0,
            len(dirty_df)-1
        )

        col = random.choice(
            dirty_df.columns
        )

        dirty_df.loc[row, col] = None

    # --------------------------
    # Blank Strings
    # --------------------------

    text_cols = [
        "Customer Name",
        "City",
        "State",
        "Supplier Name"
    ]

    existing_cols = [
        col
        for col in text_cols
        if col in dirty_df.columns
    ]

    for _ in range(errors_per_type):

        col = random.choice(existing_cols)

        idx = random.randint(
            0,
            len(dirty_df)-1
        )

        dirty_df.loc[idx, col] = ""

    # --------------------------
    # Duplicate Customer IDs
    # --------------------------

    if "Customer ID" in dirty_df.columns:

        for _ in range(errors_per_type):

            source = random.randint(
                0,
                len(dirty_df)-1
            )

            target = random.randint(
                0,
                len(dirty_df)-1
            )

            dirty_df.loc[
                target,
                "Customer ID"
            ] = dirty_df.loc[
                source,
                "Customer ID"
            ]

    # --------------------------
    # Typo Errors
    # --------------------------

    if "Customer Name" in dirty_df.columns:

        for _ in range(errors_per_type):

            idx = random.randint(
                0,
                len(dirty_df)-1
            )

            value = str(
                dirty_df.loc[
                    idx,
                    "Customer Name"
                ]
            )

            if len(value) > 3:

                pos = random.randint(
                    0,
                    len(value)-1
                )

                value = (
                    value[:pos]
                    +
                    random.choice("xyz")
                    +
                    value[pos+1:]
                )

                dirty_df.loc[
                    idx,
                    "Customer Name"
                ] = value

    # --------------------------
    # Outliers
    # --------------------------

    if "Sales Amount" in dirty_df.columns:

        for _ in range(errors_per_type):

            idx = random.randint(
                0,
                len(dirty_df)-1
            )

            dirty_df.loc[
                idx,
                "Sales Amount"
            ] *= 50

    # --------------------------
    # Inconsistent Categories
    # --------------------------

    if "Category" in dirty_df.columns:

        for _ in range(errors_per_type):

            idx = random.randint(
                0,
                len(dirty_df)-1
            )

            value = str(
                dirty_df.loc[
                    idx,
                    "Category"
                ]
            )

            dirty_df.loc[
                idx,
                "Category"
            ] = random.choice([
                value.lower(),
                value.upper(),
                value.title()
            ])

    # --------------------------
    # Negative Values
    # --------------------------

    numeric_cols = [
        "Quantity",
        "Unit Price",
        "Sales Amount",
        "Cost Price",
        "Profit"
    ]

    existing_cols = [
        col
        for col in numeric_cols
        if col in dirty_df.columns
    ]

    for _ in range(errors_per_type):

        col = random.choice(existing_cols)

        idx = random.randint(
            0,
            len(dirty_df)-1
        )

        dirty_df.loc[idx, col] = -abs(
            dirty_df.loc[idx, col]
        )

    # --------------------------
    # Duplicate Rows
    # --------------------------

    duplicate_rows = dirty_df.sample(
        max(1, rows_to_modify // 5)
    )

    dirty_df = pd.concat(
        [dirty_df, duplicate_rows],
        ignore_index=True
    )

    return dirty_df

if __name__ == "__main__":

    dataset_name = "Retail_Data"
    num_rows = 1000
    output_format = "csv"

    df = generate_dataset(
        dataset_name,
        num_rows,
        output_format
    )

    if output_format.lower() == "csv":
        df.to_csv(f"{dataset_name}.csv", index=False)

    elif output_format.lower() == "xlsx":
        df.to_excel(f"{dataset_name}.xlsx", index=False)

    else:
        raise ValueError("Unsupported format")

    print("Dataset Generated Successfully!")
    print("Rows:", len(df))
    print(f"File Saved As: {dataset_name}.{output_format}")
    print()
    print(df.head())
