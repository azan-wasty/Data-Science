# Player Performance Model ⚽🎮

> **A Python-powered EA FC player analytics tool that lets you search, compare, and visualize thousands of real player statistics through an interactive command-line interface.**

A comprehensive Python tool for analyzing **real EA FC player data** with interactive menu-driven interface and data visualization capabilities. Built with a complete dataset of EA FC players!

## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Data Requirements](#data-requirements)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 🎯 About

This is my first data science project! The Player Performance Model analyzes **real EA FC player data** containing thousands of players from the actual game. It provides an easy-to-use command-line interface for searching, filtering, comparing, and visualizing player statistics from the complete EA FC database.

**What makes this special:**
- Works with **real EA FC data** - not sample/fake data!
- Analyze thousands of actual players from the game
- Compare real player statistics and ratings
- Perfect for FIFA/EA FC fans and data science beginners

**What this tool does:**
- Search for players by name, club, or country
- Apply advanced filters (club + position + age range)
- Find top performers by various metrics
- Compare two players side-by-side
- Export filtered data to CSV
- Generate interactive plots and visualizations

## ✨ Features

### 🔍 Search & Filter
- **Player Search**: Find players by name with partial matching
- **Club Search**: Get all players from a specific team
- **Country Search**: Find players by nationality
- **Advanced Filter**: Combine multiple criteria (club, position, age range)

### 📊 Analysis & Comparison
- **Top Players**: Find top N players by any metric (OVR, SHO, PAC, DRI, DEF, PHY)
- **Player vs Player**: Direct comparison between two players
- **Visual Charts**: Bar plots for top players and line plots for comparisons

### 💾 Data Management
- **Export to CSV**: Save search results and filtered data
- **Timestamp**: Auto-generated filenames with timestamps
- **Error Handling**: Robust error handling for file operations

## 🛠️ Prerequisites

Before running this project, make sure you have:

- Python 3.7 or higher
- Required Python packages (see installation)
- EA FC player data in CSV format

## 📦 Installation

1. **Clone or download this repository**

2. **Install required packages:**
```bash
pip install pandas matplotlib
```

3. **Prepare your data:**
   - Place your EA FC CSV file in the same directory as the script
   - Rename it to `eafc.csv` (or modify the filename in the code)

## 🚀 Usage

1. **Run the application:**
```bash
python player_performance_model.py
```

2. **Navigate the menu:**
   - Choose options 1-7 for different features
   - Follow the prompts for each operation
   - Enter 0 to exit

### Example Workflow:
```
1️⃣ Search for "Messi" → View current EA FC stats
2️⃣ Find all players from "Manchester City" → Export complete squad
3️⃣ Find top 10 players by "OVR" → See the highest rated players in the game
4️⃣ Compare "Haaland" vs "Mbappé" → Real statistical comparison
5️⃣ Filter: "Premier League" + "ST" + "Age 20-25" → Find young strikers
```

## 📄 Dataset Information

This project uses a **complete EA FC player database** containing:
- ✅ **Thousands of real players** from EA FC
- ✅ **All major leagues and teams** worldwide
- ✅ **Current player ratings and statistics**
- ✅ **Comprehensive player attributes** (pace, shooting, defending, etc.)

### CSV Structure:
The dataset includes columns such as:
- `Name` - Player name
- `Team` - Current club/team
- `Nation` - Player nationality  
- `Position` - Playing position
- `Age` - Current age
- `OVR` - Overall rating (EA FC rating)
- `SHO` - Shooting rating
- `PAC` - Pace rating
- `DRI` - Dribbling rating
- `DEF` - Defending rating
- `PHY` - Physical rating
- *And potentially many more attributes depending on your dataset!*

### Sample Data:
```csv
Name,Team,Nation,Position,Age,OVR,SHO,PAC,DRI,DEF,PHY
Erling Haaland,Manchester City,Norway,ST,23,91,91,89,80,45,88
Kylian Mbappé,Paris Saint-Germain,France,ST,25,91,88,97,92,39,77
```

**Note:** Make sure your CSV file is named `eafc.csv` and placed in the same directory as the Python script.

## 🖼️ Screenshots

### Main Menu
```
──────────────────────────────────────────────────
 MAIN MENU
──────────────────────────────────────────────────
1️⃣ Search for a player by name
2️⃣ Find all players from a specific club
3️⃣ Find all players from a specific country
4️⃣ Advanced Filter: Club + Position + Age Range
5️⃣ Find top N players by metric
6️⃣ Player vs Player Comparison
7️⃣ Export data to CSV
0️⃣ Exit
```

### Sample Output
```
🔍 Enter the player's name: Haaland

✅ Found 1 player(s) matching 'Haaland':
Name: Erling Haaland | Team: Manchester City | Position: ST | Age: 23
OVR: 91 | SHO: 91 | PAC: 89 | DRI: 80 | DEF: 45 | PHY: 88

💾 Save this data to CSV? (y/n): y
✅ Data saved as 'Haaland_search.csv'
```

## 🎓 Learning Outcomes

As my first data science project, I learned:
- **Real Data Analysis**: Working with thousands of actual game records
- **Data Manipulation**: Using pandas for filtering and searching large datasets
- **User Interface**: Creating interactive command-line applications
- **Data Visualization**: Generating meaningful plots with matplotlib
- **Error Handling**: Making robust applications that handle real-world data issues
- **File I/O**: Reading large CSV files and exporting filtered results
- **Object-Oriented Programming**: Organizing complex functionality into classes
- **Sports Analytics**: Understanding player performance metrics and comparisons

## 🔮 Future Enhancements

Potential improvements for future versions:
- [ ] **Web-based interface** using Flask/Streamlit for easier access
- [ ] **Advanced analytics**: Player efficiency ratings, value-for-money analysis
- [ ] **Team chemistry analysis**: How well players work together
- [ ] **Career mode insights**: Young players with high potential
- [ ] **League comparisons**: Compare player pools across different leagues
- [ ] **Position-specific analysis**: Best players by specific positions
- [ ] **Market value integration**: Combine with transfer market data
- [ ] **Machine learning predictions**: Predict player performance trends
- [ ] **Database integration**: Store and query data more efficiently
- [ ] **Real-time updates**: Connect with EA FC API for live data

## 🤝 Contributing

This is a learning project, but feedback and suggestions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Share improvements
- Help with documentation

## 📞 Contact

If you have questions about this project or want to connect:
- Create an issue in this repository
- Share your own data science journey!

## 📚 Resources

Helpful resources I used while building this project:
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Python CSV Module](https://docs.python.org/3/library/csv.html)

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **Star this repository if you found it helpful!**

*Built with ❤️ as a first step into the world of Data Science*
