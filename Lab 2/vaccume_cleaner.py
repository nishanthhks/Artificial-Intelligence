class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.cleaned_cells = 0
        self.position = (0, 0)

    def clean(self):
        while True:
            x, y = self.position

            # Clean the current position if dirty
            if self.environment[x][y] == 'D':
                self.environment[x][y] = 'C'  # Clean the cell
                self.cleaned_cells += 1
                print(f"Cleaned position {self.position}")

            # Find next dirty cell
            next_position = self.find_next_dirty()
            if next_position:
                print(f"Moving to next dirty position {next_position}")
                self.position = next_position
            else:
                print("No more dirty cells found. Cleaning complete.")
                break

    def find_next_dirty(self):
        # Check all positions in the environment for dirty cells
        for i in range(len(self.environment)):
            for j in range(len(self.environment[i])):
                if self.environment[i][j] == 'D':
                    return (i, j)  # Return the first found dirty cell
        return None  # No dirty cells found

    def display_environment(self):
        for row in self.environment:
            print(" ".join(row))
        print(f"Total cleaned cells: {self.cleaned_cells}")


# Example usage:
initial_environment = [
    ['D', 'C', 'D', 'D'],
    ['C', 'D', 'C', 'C'],
    ['D', 'C', 'D', 'C'],
    ['C', 'C', 'C', 'D']
]

agent = VacuumCleanerAgent(initial_environment)
print("Initial environment:")
agent.display_environment()

agent.clean()

print("\nFinal environment:")
agent.display_environment()2