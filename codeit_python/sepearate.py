import pandas as pd

def process_csv(input_file, output_file): 
    # CSV 파일 읽기
    df = pd.read_csv(input_file)
    
    # C열과 D열이 모두 존재하는 행만 필터링
    df_filtered = df.dropna(subset=['C', 'D'])
    
    # D열 데이터를 ',' 기준으로 분리하여 확장
    df_expanded = df_filtered.assign(D=df_filtered['D'].str.split(','))
    df_expanded = df_expanded.explode('D')
    
    # 정리된 데이터 저장
    df_expanded.to_csv(output_file, index=False)
    
    print(f"정리된 데이터가 {output_file}에 저장되었습니다.")

# 사용 예시
input_csv = "codeit/codeit_python/제목 없는 스프레드시트 - 유레카.csv"  # 입력 파일 경로
output_csv = "/codeit_python.ouuput.csv"  # 출력 파일 경로
process_csv(input_csv, output_csv)
