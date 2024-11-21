from collections import defaultdict

def parse_domains(input_file):
    gene_domains = defaultdict(list)
    
    # 读取输入文件并存储结构域信息
    with open(input_file, 'r') as f:
        for line in f:
            fields = line.strip().split()
            gene_id = fields[0]
            start = int(fields[1])
            end = int(fields[2])
            domain_id = fields[3]
            gene_domains[gene_id].append((start, domain_id, end))
    
    return gene_domains

def format_domains(gene_domains):
    formatted_lines = []
    
    for gene_id, domains in gene_domains.items():
        # 按起始位置排序结构域
        sorted_domains = sorted(domains, key=lambda x: x[0])
        # 格式化结构域信息
        domain_str = "###".join([f"{start}={domain_id}={end}" for start, domain_id, end in sorted_domains])
        formatted_lines.append(f"{gene_id}###{domain_str}")
    
    return formatted_lines

def write_output(output_file, formatted_lines):
    with open(output_file, 'w') as f:
        for line in formatted_lines:
            f.write(line + "\n")

# 示例用法
input_file = 'add.leaf.domain.motif.txt'
output_file = 'formatted_domains.add.txt'

gene_domains = parse_domains(input_file)
formatted_lines = format_domains(gene_domains)
write_output(output_file, formatted_lines)
