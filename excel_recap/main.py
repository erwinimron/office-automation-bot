import pandas as pd

def run():
    df = pd.read_excel("data/sales.xlsx")
    df["Total"] = df["Qty"] * df["Harga"]

    summary = {
        "Total Qty": df["Qty"].sum(),
        "Total Sales": df["Total"].sum()
    }

    summary_df = pd.DataFrame([summary])
    summary_df.to_excel("output/summary.xlsx", index=False)

    print("✅ Excel recap completed")

if __name__ == "__main__":
    run()
