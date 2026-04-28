import pprint

from data import users
from validator import validate_user


def main():
    response = []
    print("Validating users...")
    for id, user in enumerate(users):
        print(f"User {id + 1}: \n")
        print(f"  {user} \n")
        response.append(validate_user(user))

    print("=" * 50)
    pprint.pprint(response)
    print("=" * 50)


if __name__ == "__main__":
    main()
