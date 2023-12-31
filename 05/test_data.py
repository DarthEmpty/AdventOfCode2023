from solution import interpret


FILENAME = "./input.txt"


class TestDataPart1:
    @classmethod
    def setup_class(cls):
        with open(FILENAME) as file:
            contents = file.read().splitlines()
        
        cls.seeds, cls.maps = interpret(contents)
    
    def test_no_gaps(self):
        """Hypothesis: there are no gaps between ranges"""
        for i, map in enumerate(TestDataPart1.maps): 
            ranges = list(map.keys())
            
            for source_range, next_range in zip(ranges[:-1], ranges[1:]):
                assert source_range.stop == next_range.start, \
                    f"Gap of size {next_range.start - source_range.stop} found in map {i}"
        