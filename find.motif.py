from Bio import SeqIO
import re

# 定义常见的FeS簇motif
#motifs = ["CxxCx10CxxCx4CxxxC", "CxxCxxCxxxC","Cx10CxxCx11C","HxxxCxxCx5C"]
#motifs = ["CxxxC"]
motifs = [
    r'C..C..C...C',r'C..C.{10}C..C.{4}C...C',
    r'C..C..C...C.{n}C..C..C...C',r'E.M.C.GGC..GG',r'MPCTCK', r'EVM.CP.GC..GG',
    r'H...C..C.....C', r'I...CP...', r'F..PC..K.',r'E...C..GC..GP',
    r'C.{1,4}C.{5,9}C...C',r'E.MACPGGC..GG',r'C.MPC.AKK',r'FTSCCP.W',
    r'C.{10,11}C..C.{11,15}C',r'TSCCP.WV',r'PC..KK',r'E.M.C..GC..GG',
    r'C..C.........C........................C...C',
    r'C.{4}C........................C...C',
    r'C..C.{8}C...C',r'C...C',
    r'CC', r'C..C', r'C..C....C...C'
]

def read_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append((record.id, str(record.seq)))
    return sequences

# 将motif转换为正则表达式
#def motif_to_regex(motif):
#    motif = motif.replace("x", ".")
#    motif = re.sub(r'(\d+)', r'.{\1}', motif)
#    return motif

# 查找motif的位置和数量，并标出motif
def find_motifs(sequence, motifs):
    motif_positions = {}
    marked_sequence = sequence

    for motif in motifs:
        #regex = motif_to_regex(motif)
        matches = [(m.start(), m.end()) for m in re.finditer(motif, sequence)]
        motif_positions[motif] = matches

        # 标出motif
        
        #for start, end in matches:
        #    marked_sequence = marked_sequence[:start] + "(" + marked_sequence[start:end] + ")" + marked_sequence[end:]

    return motif_positions, marked_sequence

# 输出motif的位置和数量
#def print_motif_info(sequence_id, motif_positions, marked_sequence):
def print_motif_info(sequence_id, motif_positions, marked_sequence):
    #print(f"Sequence ID: {sequence_id}")
    for motif, positions in motif_positions.items():
        #if len(positions)>0:
        for pos in positions:
            print(f"{sequence_id}\t{pos[0]}\t{pos[1]}\t{motif}")
            #print(f"  Motif: {motif}")
            #print(f"  Count: {len(positions)}")
            #print(f"  Positions: {positions}")
    #print("  Marked Sequence:")
    #print(f"  {marked_sequence}")
    #print()

# 主函数
def main():
    file_path = "hyd.gene.fasta" 
    sequences = read_fasta(file_path)

    for sequence_id, sequence in sequences:
        motif_positions, marked_sequence = find_motifs(sequence, motifs)
        print_motif_info(sequence_id, motif_positions, marked_sequence)
        #for motif, positions in motif_positions.items():
        #    if len(positions)>0:
        #        print(sequence_id)
if __name__ == "__main__":
    main()
