class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        #[3,2,5,1,3,4]
        skill.sort()

        week,strong=0,len(skill)-1
        sum=0
        check=skill[strong]+skill[week]

        while week<len(skill):
            if skill[week]+skill[strong]!=check:
                return -1
            sum+=(skill[strong]*skill[week])
            week+=2
            strong-=2
        return sum