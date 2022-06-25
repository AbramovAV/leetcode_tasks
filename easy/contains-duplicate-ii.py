class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val_to_idx_mapping = dict()
        for idx in range(len(nums)):
            if nums[idx] not in val_to_idx_mapping:
                val_to_idx_mapping[nums[idx]] = [idx]
            else:
                for exist_idx in val_to_idx_mapping[nums[idx]]:
                    if abs(exist_idx - idx) <= k:
                        return True
                val_to_idx_mapping[nums[idx]].append(idx)
        return False