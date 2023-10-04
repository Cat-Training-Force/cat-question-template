from hashlib import sha256

title = '天狗问答'
desc = '全部答对有 flag'
submit_text = '汪！'

# Six questions
print('按照提示输入题面和答案，每个题目一行，题目和答案之间用空格隔开。')
q1_question = input('第一题题面：')
q1_answer = input('第一题答案：')
q2_question = input('第二题题面：')
q2_answer = input('第二题答案：')
q3_question = input('第三题题面：')
q3_answer = input('第三题答案：')
q4_question = input('第四题题面：')
q4_answer = input('第四题答案：')
q5_question = input('第五题题面：')
q5_answer = input('第五题答案：')
q6_question = input('第六题题面：') 
q6_answer = input('第六题答案：')

# Calculate the hash
a = q1_answer + q2_answer + q3_answer + q4_answer + q5_answer + q6_answer
ans_hash = sha256(a.encode('utf-8')).hexdigest()

with open('config/answer-hash', 'w', encoding='utf-8') as f:
    f.write(ans_hash)

# Generate the HTML
with open('templates/main.template.html', 'r', encoding='utf-8') as f:
    template = f.read()

template = template.replace('{{title}}', title) \
    .replace('{{desc}}', desc) \
    .replace('{{submit_text}}', submit_text) \
    .replace('{{q1_question}}', q1_question) \
    .replace('{{q2_question}}', q2_question) \
    .replace('{{q3_question}}', q3_question) \
    .replace('{{q4_question}}', q4_question) \
    .replace('{{q5_question}}', q5_question) \
    .replace('{{q6_question}}', q6_question)

with open('templates/main.html', 'w', encoding='utf-8') as f:
    f.write(template)

# Test Case
'''1. 1+1=?
2
2. 2+2=?
4
3. 3+3=?
6
4. 4+4=?
8
5. 5+5=?
10
6. 6+6=?
12'''