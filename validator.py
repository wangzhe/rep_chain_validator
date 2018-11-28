from abc import abstractmethod


class AbstractValidator:
    validator_successor = None

    def set_validator_successor(self, validator_successor):
        self.validator_successor = validator_successor

    def validate(self, some_behavior):
        result = self.validate_self_logic(some_behavior)
        if result:
            if self.validator_successor is not None:
                return self.validator_successor.validate(some_behavior)
        return result

    @staticmethod
    def contain_all_element(full_list, sub_list):
        return all(elem in full_list for elem in sub_list)

    @abstractmethod
    def validate_self_logic(self, reservation):
        pass


class FromTypeValidator(AbstractValidator):
    from_type_list = ["a", "b", "c", "d"]

    def validate_self_logic(self, some_behavior):
        print("go for from type validator")
        if some_behavior is None:
            print("some behavior class error")
            return False

        # Check the full list contain both under type and exclude type
        under_from_type_list = some_behavior.under_from_type_list
        exclude_from_type_list = some_behavior.exclude_from_type_list
        if (under_from_type_list is None) or (exclude_from_type_list is None):
            print("some regarding belong type not set")
            return False

        if not self.contain_all_element(self.from_type_list, under_from_type_list):
            print("I find some from under_type, I don't know")
            return False

        if not self.contain_all_element(self.from_type_list, exclude_from_type_list):
            print("I find some exclude type, I don't know")
            return False

        # Check no overlap
        under_from_type_set = set(under_from_type_list)
        exclude_from_type_set = set(exclude_from_type_list)
        if under_from_type_set & exclude_from_type_set:
            print("Oh no, overlap")
            return False

        # Chech union is full list
        from_type_set = set(self.from_type_list)
        union_under_n_exclude = under_from_type_set.union(exclude_from_type_set)
        if from_type_set != union_under_n_exclude:
            print("Oh no, some type are not include")
            return False
        return True


class ToTypeValidator(AbstractValidator):
    to_type_list = ["x", "y", "z"]

    def validate_self_logic(self, some_behavior):
        print("go for to type validator")
        if some_behavior is None:
            print("some behavior class error")
            return False

        # Check the full list contain both under type and exclude type
        under_to_type_list = some_behavior.under_to_type_list
        exclude_to_type_list = some_behavior.exclude_to_type_list
        if (under_to_type_list is None) or (exclude_to_type_list is None):
            print("some regarding belong type not set")
            return False

        if not self.contain_all_element(self.to_type_list, under_to_type_list):
            print("I find some to under_type, I don't know")
            return False

        if not self.contain_all_element(self.to_type_list, exclude_to_type_list):
            print("I find some exclude type, I don't know")
            return False

        # Check no overlap
        under_to_type_set = set(under_to_type_list)
        exclude_to_type_set = set(exclude_to_type_list)
        if under_to_type_set & exclude_to_type_set:
            print("Oh no, overlap")
            return False

        # Chech union is full list
        from_type_set = set(self.to_type_list)
        union_under_n_exclude = under_to_type_set.union(exclude_to_type_set)
        if from_type_set != union_under_n_exclude:
            print("Oh no, some type are not include")
            return False
        return True
