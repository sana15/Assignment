
class GraduationCeremony:
    '''Graduation ceremony class '''
    def __init__(self,not_allowed_days = 4):
        '''Initialize with not allowed days'''
        self.not_allowed_days = not_allowed_days

    def attendance_probability(self,no_of_days):
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m)
        Dynamic Programing Tabulation with Space Optimization
        """

        not_allowed_days =  self.not_allowed_days
        dp_array = [1] * (not_allowed_days + 1)
        dp_array[not_allowed_days] = 0

        for i in range(1, no_of_days + 1):
            temp = [0] * (not_allowed_days + 1)
            for j in range(not_allowed_days - 1, -1, -1):
                temp[j] = dp_array[0] + dp_array[j + 1]

            temp, dp_array = dp_array, temp

        ways_to_attend_class = dp_array[0]  # total number of valid way to attend classes
        prob_miss_grad_ceremony = temp[1]  # total number of way to miss last day

        return f"{prob_miss_grad_ceremony}/{ways_to_attend_class}"



if __name__ == "__main__":
    print("Enter Number of days :")
    no_of_days = int(input())
    while no_of_days > 1:
        obj = GraduationCeremony()
        print("Probability of missing graduation Ceremony / no.of ways to attend classes over "+str(no_of_days)+" days")
        print(obj.attendance_probability(no_of_days))
        break
    else:
        print("Enter Number of days greater than 1:")
        no_of_days = int(input())
        obj = GraduationCeremony()
        print("Probability of missing graduation Ceremony / no.of ways to attend classes over "+str(no_of_days)+" days")
        print(obj.attendance_probability(no_of_days))



