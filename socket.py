
import socket

def check_port(host, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            return "OPEN"
        elif result == 111 or result == 10061:
            return "CLOSED"
        else:
            return "FILTERED"

    except socket.timeout:
        return "FILTERED"
    except OSError:
        return "FILTERED"


def main():
    print("===================================")
    print("       PORT STATUS CHECKER")
    print("===================================")

    host = "127.0.0.1"

    print("Target Host:", host)

    try:
        start = int(input("Enter starting port: "))
        end = int(input("Enter ending port: "))
        timeout = float(input("Enter timeout (seconds): "))

        if start < 1 or end > 65535 or start > end or timeout <= 0:
            print("Invalid input!")
            return

    except ValueError:
        print("Please enter valid numbers!")
        return

    open_count = 0
    closed_count = 0
    filtered_count = 0

    print("\n-----------------------------------")
    print("PORT\t\tSTATUS")
    print("-----------------------------------")

    for port in range(start, end + 1):

        status = check_port(host, port, timeout)

        print(f"{port}\t\t{status}")

        if status == "OPEN":
            open_count += 1
        elif status == "CLOSED":
            closed_count += 1
        else:
            filtered_count += 1

    print("-----------------------------------")
    print("PORT SCAN SUMMARY")
    print("-----------------------------------")

    print("Open Ports     :", open_count)
    print("Closed Ports   :", closed_count)
    print("Filtered Ports :", filtered_count)

    print("-----------------------------------")
    print("CHECK COMPLETED")
    print("-----------------------------------")


if __name__ == "__main__":
    main()
