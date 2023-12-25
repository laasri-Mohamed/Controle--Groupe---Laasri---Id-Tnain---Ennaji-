import random

# A task instance
class TaskIns(object):

    # Constructor (should only be invoked with keyword parameters)
    def __init__(self, start, end, priority, name):
        self.start = start
        self.end = end
        self.usage = 0
        self.priority = priority
        self.name = name.replace("\n", "")
        self.id = int(random.random() * 10000)

    def use(self, usage):
        self.usage += usage
        if self.usage >= self.end - self.start:
            return True
        return False

    def __repr__(self):
        return str(self.name) + "#" + str(self.id) + " - start: " + str(self.start) + " priority: " + str(
            self.priority)

    def get_unique_name(self):
        return str(self.name) + "#" + str(self.id)


# Task types
class TaskType(object):
    def __init__(self, period, release, execution, deadline, name):
        self.period = period
        self.release = release
        self.execution = execution
        self.deadline = deadline
        self.name = name

    @classmethod
    def tasktype_cmp(cls, self, other):
        if self.deadline < other.deadline:
            return -1
        if self.deadline > other.deadline:
            return 1
        return 0


def priority_cmp(one, other):
    if one.priority < other.priority:
        return -1
    elif one.priority > other.priority:
        return 1
    return 0