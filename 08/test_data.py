from solution import interpret, path_gen


FILENAME = "./input.txt"


class TestDataPart2:
    @classmethod
    def setup_class(cls):
        with open(FILENAME) as file:
            contents = file.read().splitlines()
    
        cls.directions, cls.network = interpret(contents)
    
    def test_loop(self):
        """Hypothesis: Paths loop back on themselves"""
        start_nodes = [
            node for node in TestDataPart2.network
            if node.endswith("A")
        ]
        
        for start_node in start_nodes:
            path_nodes = path_gen(
                start_node,
                TestDataPart2.directions,
                TestDataPart2.network
            )
            
            path = []
            
            while not (current_node := next(path_nodes)[1]).endswith("Z"):
                path.append(current_node)
            
            assert next(path_nodes)[1] in path, \
                f"Path starting with {start_node} does not loop after destination {current_node} found."
            
            