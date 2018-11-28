from validator import FromTypeValidator, ToTypeValidator


class Reservation:
    source_type = None
    reservation_type = None

    def __init__(self, source_type, reservation_type) -> None:
        super().__init__()
        self.source_type = source_type
        self.reservation_type = reservation_type


class AbstractTypeBehavior:
    under_from_type_list = None
    exclude_from_type_list = None

    under_to_type_list = None
    exclude_to_type_list = None

    my_action = "behavior action"

    def __init__(self, under_from_type_list, exclude_from_type_list, under_to_type_list, exclude_to_type_list) -> None:
        super().__init__()
        self.under_from_type_list = under_from_type_list
        self.exclude_from_type_list = exclude_from_type_list
        self.under_to_type_list = under_to_type_list
        self.exclude_to_type_list = exclude_to_type_list

    def check_create_successful(self):
        my_behavior_from_type_validator = FromTypeValidator()
        my_behavior_to_type_validator = ToTypeValidator()
        my_behavior_from_type_validator.set_validator_successor(my_behavior_to_type_validator)
        my_behavior_from_type_validator.validate(self)

    def is_in_list(self, reservation):
        if not (reservation.source_type in self.under_from_type_list):
            print("from type in list, so no further action")
            return False
        return True


# Engineer need to write the class of behavior
class SomeTypeBehavior(AbstractTypeBehavior):

    def action(self, reservation):
        if not self.is_in_list(reservation):
            return
        print(self.my_action)


def setup_new_behavior():
    # Engineer setup the new behavior and check
    new_type_behavior = SomeTypeBehavior(["a", "b", "d"], ["c"], ["x"], ["y", "z"])
    new_type_behavior.check_create_successful()
    return new_type_behavior


my_new_type_behavior = setup_new_behavior()
# API code
my_new_type_behavior.action(Reservation(source_type="a", reservation_type="x"))



