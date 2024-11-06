import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set dark theme for all plots
plt.style.use('dark_background')

# Load the dataset
renewable_energy_data_path = 'global_renewable_energy_production.csv'
renewable_energy_data = pd.read_csv(renewable_energy_data_path)


def data_summary_statistics(data):
    """
    Generates summary statistics for the dataset, including descriptive statistics,
    correlation, kurtosis, and skewness.
    """
    # Descriptive Statistics
    print("Descriptive Statistics:\n", data.describe(include='all'))

    # Selecting only numerical columns for correlation, kurtosis, and skewness
    numerical_data = data.select_dtypes(include=['float64', 'int64'])

    # Correlation Matrix
    correlation_matrix = numerical_data.corr()
    print("\nCorrelation Matrix:\n", correlation_matrix)

    # Kurtosis and Skewness
    kurtosis_values = numerical_data.kurtosis()
    skewness_values = numerical_data.skew()
    print("\nKurtosis Values:\n", kurtosis_values)
    print("\nSkewness Values:\n", skewness_values)


def plot_line_chart(data, start_year, end_year):
    """
    Plots a line chart for total renewable energy production between specified years for the top 5 countries.
    """
    # Calculate average total renewable energy production by country and select top 5
    avg_energy_by_country = data.groupby('Country')['TotalRenewableEnergy'].mean().nlargest(5).index
    filtered_data = data[(data['Year'] >= start_year) & (data['Year'] <= end_year) & (data['Country'].isin(avg_energy_by_country))]
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=filtered_data, x='Year', y='TotalRenewableEnergy', hue='Country', palette='bright')
    plt.xlabel('Year', fontsize=12, fontweight='bold', color='white')
    plt.ylabel('Total Renewable Energy Production', fontsize=12, fontweight='bold', color='white')
    plt.title(f'Trend of Total Renewable Energy Production ({start_year}-{end_year}) by Top 5 Countries', fontsize=14, fontweight='bold', color='white')
    plt.legend(title='Country', title_fontsize=12, fontsize=10, loc='upper left', frameon=True)
    plt.show()


def plot_bar_chart(data):
    """
    Plots a bar chart for average renewable energy production by country with professional styling.
    """
    avg_energy_by_country = data.groupby('Country')['TotalRenewableEnergy'].mean().reset_index()
    plt.figure(figsize=(14, 8))
    sns.barplot(data=avg_energy_by_country, x='Country', y='TotalRenewableEnergy', palette='viridis')
    plt.xlabel('Country', fontsize=14, fontweight='bold', color='white')
    plt.ylabel('Average Total Renewable Energy Production', fontsize=14, fontweight='bold', color='white')
    plt.title('Average Total Renewable Energy Production by Country', fontsize=16, fontweight='bold', color='white')
    plt.xticks(fontsize=12, fontweight='bold', rotation=45, color='white')
    plt.yticks(fontsize=12, color='white')
    plt.grid(axis='y', linestyle='--', linewidth=0.7)
    plt.tight_layout()
    plt.show()


def plot_heatmap(data):
    """
    Plots a heatmap of the correlation matrix for renewable energy types.
    """
    numerical_data = data.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(10, 6))
    correlation_matrix = numerical_data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, annot_kws={"size": 10})
    plt.title('Heatmap of Correlation Between Different Types of Renewable Energy Production', fontsize=14, fontweight='bold', color='white')
    plt.xticks(fontsize=10, fontweight='bold', color='white')
    plt.yticks(fontsize=10, fontweight='bold', rotation=0, color='white')
    plt.show()


def plot_pie_chart(data):
    """
    Plots a pie chart showing the proportion of different types of renewable energy production.
    """
    energy_types = ['SolarEnergy', 'WindEnergy', 'HydroEnergy', 'OtherRenewableEnergy']
    total_energy = data[energy_types].sum()
    plt.figure(figsize=(10, 8))
    plt.pie(total_energy, labels=energy_types, autopct='%1.1f%%', colors=sns.color_palette('dark'))
    plt.title('Proportion of Different Types of Renewable Energy Production', fontsize=16, fontweight='bold', color='white')
    plt.tight_layout()
    plt.show()


# Step 1: Generate Summary Statistics
data_summary_statistics(renewable_energy_data)

# Step 2: Generate Visualizations
plot_line_chart(renewable_energy_data, 2018, 2022)
plot_bar_chart(renewable_energy_data)
plot_heatmap(renewable_energy_data)
plot_pie_chart(renewable_energy_data)