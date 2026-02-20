class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for r in range(len(image)):
            image[r]=image[r][::-1]

        for row in range(len(image)):
            for c in range(len(image[row])):
                if image[row][c]==0:
                    image[row][c]=1
                else:
                    image[row][c]=0
        return image



        
        