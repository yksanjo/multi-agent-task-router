from src.project_profile import PROJECT_NAME
from src.service_contract import build_status, status_payload


def main() -> None:
    status = build_status(PROJECT_NAME)
    print(status_payload(status))


if __name__ == "__main__":
    main()
