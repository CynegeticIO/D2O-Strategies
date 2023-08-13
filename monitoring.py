import time
import matplotlib.pyplot as plt
import threading

class InvestmentManager:
    def __init__(self, strategy, data_processor, algorithm):
        self.strategy = strategy
        self.data_processor = data_processor
        self.algorithm = algorithm
        self.live_data = []  # To store live data for visualization
        self.running = False

    def fetch_live_data(self):
        while self.running:
            live_data = self.data_processor.fetch_real_time_data(self.strategy.assets)
            self.live_data.append(live_data)
            time.sleep(5)  # Fetch data every 5 seconds

    def visualize_live_data(self):
        while self.running:
            if self.live_data:
                latest_data = self.live_data[-1]
                # Visualize the latest data using matplotlib
                plt.figure(figsize=(10, 6))
                # Plot your data here (e.g., price, moving averages, etc.)
                plt.title("Live Data Visualization")
                plt.xlabel("Time")
                plt.ylabel("Value")
                plt.grid(True)
                plt.show(block=False)
                plt.pause(5)  # Update plot every 5 seconds
            else:
                print("No live data available yet.")
                time.sleep(5)

    def start_monitoring(self):
        print("Starting monitoring...")
        self.running = True
        data_fetch_thread = threading.Thread(target=self.fetch_live_data)
        data_visualize_thread = threading.Thread(target=self.visualize_live_data)
        data_fetch_thread.start()
        data_visualize_thread.start()

    def stop_monitoring(self):
        print("Stopping monitoring...")
        self.running = False


