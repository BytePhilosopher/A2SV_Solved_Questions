class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        sto = {}   # content -> list of file paths
        
        for path in paths:
            path = path.split()
            dir = path[0]
            
            for file_info in path[1:]:
                op_ind = file_info.find("(")
                clo_ind = file_info.find(")")
                
                con = file_info[op_ind + 1 : clo_ind]
                filename = file_info[:op_ind]
                file_path = dir + "/" + filename
                
                if con not in sto:
                    sto[con] = []
                sto[con].append(file_path)
        
        return [files for files in sto.values() if len(files) > 1]
