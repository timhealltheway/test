import argparse
import pandas as pd
from datetime import datetime, timedelta
from statistics import mean, stdev


sleep_time_seconds = 0.017

def parse_console_args(parser):
    parser.add_argument('--received_file', help='file generated by receive.py', required=True)
    parser.add_argument('--sent_file', help='file generated by send.py', required=True)
    return parser.parse_args()

def parse_receive_file(file_path):
    data = pd.read_csv(file_path)
    received_at_times = list(map(lambda t: datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f"), data["received_at"].values))
    return received_at_times

def extract_generated_packet_indexes(received_data_file_path):
    data = pd.read_csv(received_data_file_path)
    is_predicted_list = list(data["is_predicted"].values)
    generated_indexes = []
    for i in range(len(is_predicted_list)):
        if is_predicted_list[i]:
            generated_indexes.append(i)
    return generated_indexes



def parse_send_file(file_path):
    data = pd.read_csv(file_path)
    sent_at_times = list(map(lambda t: datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f"), data["sent_at"].values))
    return sent_at_times

def calculate_packet_end_to_end(sent_at_times, received_at_times, generated_indexes, generated_only = True):
    #function to account for sleep time included for generated packets
    end_to_end_times = []
    for i in range(len(sent_at_times)):
        end_to_end_time = timedelta.total_seconds(received_at_times[i] - sent_at_times[i])
        if i in generated_indexes:
            end_to_end_time -= sleep_time_seconds
            if generated_only:
                end_to_end_times.append(end_to_end_time)
        if not generated_only:
            end_to_end_times.append(end_to_end_time)
    return end_to_end_times

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog='speed-statistics',
                        description='Receives pmu packets',
                        epilog='Text at the bottom of help')
    args = parse_console_args(parser)
    end_to_end_times = calculate_packet_end_to_end(parse_send_file(args.sent_file), parse_receive_file(args.received_file), extract_generated_packet_indexes(args.received_file))
    for i in range(len(end_to_end_times)):
        if end_to_end_times[i] < 0:
            print(i)
    print("Mean time: " + str(mean(end_to_end_times)))
    print("Smallest time: " + str(min(end_to_end_times)))
    print("Max time: " + str(max(end_to_end_times)))
    print("Std dev: " + str(stdev(end_to_end_times)))