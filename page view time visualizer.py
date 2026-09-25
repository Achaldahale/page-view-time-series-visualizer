    df_bar["month"] = df_bar.index.month

    # Calculate average page views
    df_bar = (
        df_bar
        .groupby(["year", "month"])["value"]
        .mean()
        .unstack()
    )

    # Create bar plot
    fig = df_bar.plot(
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_line_plot():
    # Import data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

    # Set date as index
    df.set_index("date", inplace=True)

    # Clean data
    df = df[
        (df["value"] >= df["value"].quantile(0.025))
        & (df["value"] <= df["value"].quantile(0.975))
    ]

    # Create line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df["value"])

    ax.set_title(
        "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save and return
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Import data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

    # Set date as index
    df.set_index("date", inplace=True)

    # Clean data
    df = df[
        (df["value"] >= df["value"].quantile(0.025))
        & (df["value"] <= df["value"].quantile(0.975))
    ]

    # Copy dataframe
    df_bar = df.copy()

    # Extract year and month
    df_bar["year"] = df_bar.index.year

        kind="bar",
        figsize=(12, 8)
    ).get_figure()

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")

    # Month labels
    plt.legend(
        title="Months",
        labels=[
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]
    )

    # Save and return
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Import data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

    # Set date as index
    df.set_index("date", inplace=True)

    # Clean data
    df = df[
        (df["value"] >= df["value"].quantile(0.025))
        & (df["value"] <= df["value"].quantile(0.975))
    ]

    # Copy dataframe
    df_box = df.copy()

    # Prepare data for box plots
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")

    # Set month order
    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    # Create figure
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise box plot
    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        ax=axes[0]
    )

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        order=month_order,
        ax=axes[1]
    )

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save and return
    fig.savefig("box_plot.png")
    return fig