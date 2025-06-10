class SONETFrame:
    def __init__(self, sts_level=1):
        self.sts_level = sts_level  # STS-1, STS-3, etc.
        self.payload = bytearray(810 * sts_level)  # SONET frame size

    def add_overhead(self):
        """Add SONET transport overhead"""
        self.payload[0:3] = b'\xF6\x28\x3F'  # A1/A2 framing bytes

# Usage
frame = SONETFrame(sts_level=3)  # STS-3 frame (155.52 Mbps)
frame.add_overhead()
