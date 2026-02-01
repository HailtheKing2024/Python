import math


class Lead:
    """Represents a sales lead and provides a lead_score used for comparisons.

    Comparison operators compare Lead instances by their `lead_score()`.
    If compared with a non-Lead object, NotImplemented is returned so Python
    can try reflected operations or raise a TypeError.
    """

    def __init__(self, name, staff_size, estimated_revenue, effort_factor):
        self.name = name
        self.staff_size = staff_size
        self.estimated_revenue = estimated_revenue
        self.effort_factor = effort_factor

    def lead_score(self):
        """Compute the lead score according to the original formula.

        Formula:
            1 / (staff_size / estimated_revenue * 10**(digit_len(rev)-digit_len(staff_size)) * effort_factor)
        """
        return 1 / (
            self.staff_size
            / self.estimated_revenue
            * (
                10
                ** (
                    self.__digit_length(self.estimated_revenue)
                    - self.__digit_length(self.staff_size)
                )
            )
            * self.effort_factor
        )

    def __digit_length(self, num):
        # number of digits in the integer part of num
        return len(str(math.floor(num)))

    def __eq__(self, other):
        if not isinstance(other, Lead):
            return NotImplemented
        return self.lead_score() == other.lead_score()

    def __ne__(self, other):
        if not isinstance(other, Lead):
            return NotImplemented
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Lead):
            return NotImplemented
        return self.lead_score() < other.lead_score()

    def __le__(self, other):
        if not isinstance(other, Lead):
            return NotImplemented
        return self.lead_score() <= other.lead_score()

    def __gt__(self, other):
        if not isinstance(other, Lead):
            return NotImplemented
        return self.lead_score() > other.lead_score()

    def __ge__(self, other):
        if not isinstance(other, Lead):
            return NotImplemented
        return self.lead_score() >= other.lead_score()

    def __repr__(self):
        return f"Lead(name={self.name!r}, score={self.lead_score():.6g})"
