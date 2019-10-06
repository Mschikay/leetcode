class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1
        for node in preorder.split(","):
            slot -= 1
            if slot < 0:
                return False
            if node != "#":
                slot += 2
        return not slot