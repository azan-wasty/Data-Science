import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

class PlayerPerformanceModel:
    def __init__(self, csv_file='eafc.csv'):
        """Initialize the Player Performance Model"""
        self.csv_file = csv_file
        self.df = None
        self.load_data()
        
    def load_data(self):
        """Load the dataset with error handling"""
        try:
            self.df = pd.read_csv(self.csv_file)
            print(f" Successfully loaded {len(self.df)} players from {self.csv_file}")
        except FileNotFoundError:
            print(f" Error: File '{self.csv_file}' not found.")
            print("Please make sure the CSV file is in the same directory as this script.")
            exit(1)
        except Exception as e:
            print(f"Error loading data: {e}")
            exit(1)
    
    def display_welcome(self):
        """Display welcome message"""
        print("=" * 60)
        print(" WELCOME TO THE PLAYER PERFORMANCE MODEL ")
        print("=" * 60)
        print("This model will help you analyze player performance based on various metrics.")
        print()
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "─" * 50)
        print(" MAIN MENU")
        print("─" * 50)
        print("1️  Search for a player by name")
        print("2️  Find all players from a specific club")
        print("3️  Find all players from a specific country")
        print("4️  Advanced Filter: Club + Position + Age Range")
        print("5️  Find top N players by metric (OVR, SHO, PAC, DRI, DEF, PHY)")
        print("6️  Player vs Player Comparison")
        print("7️  Export data to CSV")
        print("0️  Exit")
        print("─" * 50)
    
    def get_user_choice(self):
        """Get and validate user input"""
        while True:
            try:
                choice = input("Enter your choice (0-7): ").strip()
                if choice in ['0', '1', '2', '3', '4', '5', '6', '7']:
                    return int(choice)
                else:
                    print(" Invalid choice. Please enter a number between 0-7.")
            except KeyboardInterrupt:
                print("\n\n Goodbye!")
                exit(0)
            except Exception:
                print(" Invalid input. Please enter a number.")
    
    def search_by_name(self):
        """Search for players by name"""
        player_name = input("🔍 Enter the player's name: ").strip()
        if not player_name:
            print(" Please enter a valid name.")
            return
            
        player_data = self.df[self.df['Name'].str.contains(player_name, case=False, na=False)]
        
        if not player_data.empty:
            print(f"\n Found {len(player_data)} player(s) matching '{player_name}':")
            self.display_results(player_data)
            self.offer_save(player_data, f"{player_name}_search")
        else:
            print(f" No player found matching '{player_name}'.")
    
    def search_by_club(self):
        """Search for players by club"""
        club_name = input("  Enter the club name: ").strip()
        if not club_name:
            print(" Please enter a valid club name.")
            return
            
        club_data = self.df[self.df['Team'].str.contains(club_name, case=False, na=False)]
        
        if not club_data.empty:
            print(f"\n Found {len(club_data)} player(s) from '{club_name}':")
            self.display_results(club_data)
            self.offer_save(club_data, f"{club_name}_players")
        else:
            print(f" No players found from '{club_name}'.")
    
    def search_by_country(self):
        """Search for players by country"""
        country_name = input(" Enter the country name: ").strip()
        if not country_name:
            print(" Please enter a valid country name.")
            return
            
        country_data = self.df[self.df['Nation'].str.contains(country_name, case=False, na=False)]
        
        if not country_data.empty:
            print(f"\n Found {len(country_data)} player(s) from '{country_name}':")
            self.display_results(country_data)
            self.offer_save(country_data, f"{country_name}_players")
        else:
            print(f" No players found from '{country_name}'.")
    
    def advanced_filter(self):
        """Filter players by multiple criteria"""
        print("\n🔧 Advanced Filter Setup:")
        
        try:
            club_name = input("Club name (press Enter to skip): ").strip()
            position = input("Position (press Enter to skip): ").strip()
            
            age_min_input = input("Minimum age (press Enter to skip): ").strip()
            age_min = int(age_min_input) if age_min_input else None
            
            age_max_input = input("Maximum age (press Enter to skip): ").strip()
            age_max = int(age_max_input) if age_max_input else None
            
        except ValueError:
            print("❌ Invalid age input. Please enter valid numbers.")
            return
        
        # Apply filters
        filtered_data = self.df.copy()
        
        if club_name:
            filtered_data = filtered_data[filtered_data['Team'].str.contains(club_name, case=False, na=False)]
        if position:
            filtered_data = filtered_data[filtered_data['Position'].str.contains(position, case=False, na=False)]
        if age_min is not None:
            filtered_data = filtered_data[filtered_data['Age'] >= age_min]
        if age_max is not None:
            filtered_data = filtered_data[filtered_data['Age'] <= age_max]
        
        if not filtered_data.empty:
            print(f"\n Found {len(filtered_data)} player(s) matching your criteria:")
            self.display_results(filtered_data)
            self.offer_save(filtered_data, "filtered_players")
        else:
            print("❌ No players found matching the specified criteria.")
    
    def find_top_players(self):
        """Find top N players by specific metric"""
        valid_metrics = ['OVR', 'SHO', 'PAC', 'DRI', 'DEF', 'PHY']
        
        print(f"\n Available metrics: {', '.join(valid_metrics)}")
        metric = input("Enter metric: ").strip().upper()
        
        if metric not in valid_metrics:
            print(f" Invalid metric. Please choose from: {', '.join(valid_metrics)}")
            return
        
        try:
            top_n = int(input("Enter number of top players (1-50): "))
            if top_n < 1 or top_n > 50:
                raise ValueError()
        except ValueError:
            print(" Please enter a valid number between 1 and 50.")
            return
        
        # Check if metric column exists and has valid data
        if metric not in self.df.columns:
            print(f" Metric '{metric}' not found in the dataset.")
            return
            
        top_players = self.df.nlargest(top_n, metric)
        
        if not top_players.empty:
            print(f"\n Top {top_n} players by {metric}:")
            self.display_results(top_players[['Name', 'Team', 'Position', metric]], show_index=True)
            self.offer_save(top_players, f"top_{top_n}_{metric}")
            self.offer_plot(top_players, metric, top_n)
        else:
            print(" No players found.")
    
    def compare_players(self):
        """Compare two players"""
        player1_name = input(" Enter the name of the first player: ").strip()
        player2_name = input(" Enter the name of the second player: ").strip()
        
        if not player1_name or not player2_name:
            print(" Please enter valid player names.")
            return
        
        player1_data = self.df[self.df['Name'].str.contains(player1_name, case=False, na=False)]
        player2_data = self.df[self.df['Name'].str.contains(player2_name, case=False, na=False)]
        
        if player1_data.empty:
            print(f" Player '{player1_name}' not found.")
            return
        if player2_data.empty:
            print(f" Player '{player2_name}' not found.")
            return
        
        # Get the first match for each player
        player1 = player1_data.iloc[0]
        player2 = player2_data.iloc[0]
        
        print(f"\n Comparison: {player1['Name']} vs {player2['Name']}")
        print("=" * 60)
        
        metrics = ['OVR', 'SHO', 'PAC', 'DRI', 'DEF', 'PHY']
        comparison_data = []
        
        for metric in metrics:
            if metric in self.df.columns:
                p1_val = player1[metric]
                p2_val = player2[metric]
                winner = player1['Name'] if p1_val > p2_val else player2['Name'] if p2_val > p1_val else "Tie"
                comparison_data.append({
                    'Metric': metric,
                    player1['Name']: p1_val,
                    player2['Name']: p2_val,
                    'Winner': winner
                })
        
        if comparison_data:
            comparison_df = pd.DataFrame(comparison_data)
            print(comparison_df.to_string(index=False))
            self.offer_comparison_plot(player1, player2, metrics)
    
    def export_data(self):
        """Export current dataset or filtered data"""
        print("\n Export Options:")
        print("1. Export entire dataset")
        print("2. Export sample data (first 100 players)")
        
        choice = input("Choose export option (1-2): ").strip()
        
        if choice == '1':
            data_to_export = self.df
            filename = f"full_dataset_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        elif choice == '2':
            data_to_export = self.df.head(100)
            filename = f"sample_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        else:
            print(" Invalid choice.")
            return
        
        try:
            data_to_export.to_csv(filename, index=False)
            print(f" Data exported successfully as '{filename}'")
        except Exception as e:
            print(f"❌ Error exporting data: {e}")
    
    def display_results(self, data, show_index=False):
        """Display search results in a formatted way"""
        if show_index:
            for i, (_, player) in enumerate(data.iterrows(), 1):
                print(f"\n{i}. {player['Name']} ({player.get('Team', 'N/A')})")
                if 'Position' in player:
                    print(f"   Position: {player['Position']} | Age: {player.get('Age', 'N/A')}")
                # Show available metrics
                metrics = ['OVR', 'SHO', 'PAC', 'DRI', 'DEF', 'PHY']
                metric_str = " | ".join([f"{m}: {player.get(m, 'N/A')}" for m in metrics if m in player])
                if metric_str:
                    print(f"   {metric_str}")
        else:
            print(data.to_string(index=False))
    
    def offer_save(self, data, default_filename):
        """Offer to save data to CSV"""
        save_choice = input(f"\n💾 Save this data to CSV? (y/n): ").strip().lower()
        if save_choice in ['y', 'yes']:
            filename = input(f"Enter filename (default: {default_filename}.csv): ").strip()
            if not filename:
                filename = f"{default_filename}.csv"
            elif not filename.endswith('.csv'):
                filename += '.csv'
            
            try:
                data.to_csv(filename, index=False)
                print(f" Data saved as '{filename}'")
            except Exception as e:
                print(f" Error saving file: {e}")
    
    def offer_plot(self, data, metric, top_n):
        """Offer to create a plot for top players"""
        plot_choice = input(f"\n📊 Create a plot for top {top_n} players by {metric}? (y/n): ").strip().lower()
        if plot_choice in ['y', 'yes']:
            self.create_top_players_plot(data, metric, top_n)
    
    def create_top_players_plot(self, data, metric, top_n):
        """Create a bar plot for top players"""
        try:
            plt.figure(figsize=(12, 8))
            plt.bar(range(len(data)), data[metric], color='skyblue', edgecolor='navy', alpha=0.7)
            plt.title(f'Top {top_n} Players by {metric}', fontsize=16, fontweight='bold')
            plt.xlabel('Players', fontsize=12)
            plt.ylabel(metric, fontsize=12)
            plt.xticks(range(len(data)), data['Name'], rotation=45, ha='right')
            plt.grid(axis='y', alpha=0.3)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"❌ Error creating plot: {e}")
    
    def offer_comparison_plot(self, player1, player2, metrics):
        """Offer to create a comparison plot"""
        plot_choice = input(f"\n📊 Create a comparison plot? (y/n): ").strip().lower()
        if plot_choice in ['y', 'yes']:
            self.create_comparison_plot(player1, player2, metrics)
    
    def create_comparison_plot(self, player1, player2, metrics):
        """Create a comparison plot between two players"""
        try:
            player1_values = [player1.get(metric, 0) for metric in metrics]
            player2_values = [player2.get(metric, 0) for metric in metrics]
            
            plt.figure(figsize=(12, 8))
            plt.plot(metrics, player1_values, marker='o', linewidth=3, label=player1['Name'], color='blue')
            plt.plot(metrics, player2_values, marker='s', linewidth=3, label=player2['Name'], color='red')
            plt.title(f"Player Comparison: {player1['Name']} vs {player2['Name']}", fontsize=16, fontweight='bold')
            plt.xlabel('Metrics', fontsize=12)
            plt.ylabel('Rating', fontsize=12)
            plt.legend(fontsize=12)
            plt.grid(True, alpha=0.3)
            plt.ylim(0, 100)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"❌ Error creating comparison plot: {e}")
    
    def run(self):
        """Main application loop"""
        self.display_welcome()
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == 0:
                print("\n Thank you for using the Player Performance Model!")
                print("Goodbye! ")
                break
            elif choice == 1:
                self.search_by_name()
            elif choice == 2:
                self.search_by_club()
            elif choice == 3:
                self.search_by_country()
            elif choice == 4:
                self.advanced_filter()
            elif choice == 5:
                self.find_top_players()
            elif choice == 6:
                self.compare_players()
            elif choice == 7:
                self.export_data()
            
            # Ask if user wants to continue
            if choice != 0:
                continue_choice = input("\n Perform another operation? (y/n): ").strip().lower()
                if continue_choice not in ['y', 'yes']:
                    print("\n Thank you for using the Player Performance Model!")
                    print("Goodbye! ")
                    break

def main():
    """Main function to run the application"""
    try:
        model = PlayerPerformanceModel('eafc.csv')
        model.run()
    except KeyboardInterrupt:
        print("\n\n Application interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please check your CSV file and try again.")

if __name__ == "__main__":
    main()
