import logging

LOGGER = logging.getLogger()

def main():
    print("Hello from autils!")

if __name__ == "__main__":
    main()
    hi = "hi"
    LOGGER.warning("%s", hi)

