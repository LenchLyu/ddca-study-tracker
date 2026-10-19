"""Export portable task JSON to UTF-8 CSV files using only the standard library."""

import csv
import json
from collections import Counter
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    tasks = json.loads((root / 'data/tasks.json').read_text(encoding='utf-8'))
    codes = {task['code'] for task in tasks}
    if len(codes) != len(tasks):
        raise ValueError('Task codes must be unique')
    for task in tasks:
        for relation in ('prereq', 'related'):
            missing = set(task.get(relation, [])) - codes
            if missing:
                raise ValueError(f"{task['code']}: unknown {relation} codes {missing}")

    fields = [
        '任务名称', '编号', '官方顺序', '任务类型', '所属阶段', '资料年份',
        '学习优先级', '状态', '掌握程度', '官方资料链接', '答案链接',
        '视频链接', '完成标准', '验证范围', '资料核对',
        '前置任务编号', '相关任务编号',
    ]
    with (root / 'data/tasks.csv').open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for task in tasks:
            row = {field: task['properties'].get(field, '') for field in fields}
            row['前置任务编号'] = '; '.join(task.get('prereq', []))
            row['相关任务编号'] = '; '.join(task.get('related', []))
            writer.writerow(row)

    with (root / 'data/study-log.csv').open('w', encoding='utf-8-sig', newline='') as handle:
        csv.writer(handle).writerow([
            '记录名称', '日期', '关联任务编号', '本次用时（分钟）',
            '本次完成了什么', '遇到的问题', '下一步行动',
        ])

    print(json.dumps({
        'tasks': len(tasks),
        'categories': dict(Counter(task['properties']['任务类型'] for task in tasks)),
        'study_log_rows': 0,
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
