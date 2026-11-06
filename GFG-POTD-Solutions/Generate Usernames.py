
class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        reserved = set(arr)
        next_suffix = {}
        result = []

        for name in arr:
            if name not in next_suffix:
                next_suffix[name] = 1
                result.append(name)
            else:
                suffix = next_suffix[name]

                while name + str(suffix) in reserved:
                    suffix += 1

                new_name = name + str(suffix)
                reserved.add(new_name)

                next_suffix[name] = suffix + 1
                result.append(new_name)

        return result
