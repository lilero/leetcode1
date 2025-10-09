class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 哈希表
        # 创建一个空字典用于存储字母异位词分组
        d = {}
        # 遍历输入的字符串列表
        for s in strs:
            # 对每个字符串的字符进行排序，生成统一的键
            # 例如: "eat" 和 "tea" 排序后都变成 "aet"
            s_ = "".join(sorted(s))
            # 检查排序后的字符串是否已存在于字典中
            if s_ in d:
                # 如果存在，将原字符串添加到对应的列表中
                d[s_].append(s)
            else:
                # 如果不存在，创建一个新的列表存储该字符串
                d[s_] = [s]
        # 将字典中所有的值（列表）转换为列表并返回
        return list(d.values())
