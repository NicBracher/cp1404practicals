"""
CP1404 Practical 7 - Project Management

"""

class Project:
    """Represent a project with its details."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        """Return string representation of the Project."""
        return f"{self.name}, Start date: {self.start_date.strftime('%d/%m/%Y')}, Priority: {self.priority}, Cost estimate: ${self.cost_estimate:.2f}, Percent complete: {self.percent_complete}%"