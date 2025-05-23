# accounts/views.py

from django.shortcuts import render
from .forms import StudentBatchCreateForm
from .models import CustomUser
from django.contrib.auth.hashers import make_password
import random, string

#　　初期パスワードを生成
def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

#　　学籍番号を生成（例: A2442001）
def generate_student_id(prefix, year, department_code, index):
    yy = str(year)[-2:]                # 入学年（下2桁）
    dd = str(department_code).zfill(2) # 学科コード（2桁）
    nnn = str(index).zfill(3)          # 通し番号（3桁）
    return f"{prefix}{yy}{dd}{nnn}"

# 　大学職員向け：新入生アカウント一括発行ビュー
def student_batch_create_view(request):
    if request.method == 'POST':
        # POSTされたフォームデータをバリデーション
        form = StudentBatchCreateForm(request.POST)

        if form.is_valid():
            # フォーム入力値の取得
            year = form.cleaned_data['year']
            dept_code = int(form.cleaned_data['department'])
            count = form.cleaned_data['count']
            prefix = form.cleaned_data['prefix']

            created_users = []

            # 　人数分、アカウントを生成
            for i in range(1, count + 1):
                student_id = generate_student_id(prefix, year, dept_code, i)
                password = generate_password()

                # 　CustomUser を作成（パスワードはハッシュ化）
                user = CustomUser.objects.create(
                    username=student_id,
                    user_type='student',
                    password=make_password(password)
                )

                # 　作成したIDとパスワードをリストに追加（後で表示用）
                created_users.append((student_id, password))

            # 　結果ページへ（生成済みユーザーの一覧を表示）
            return render(request, 'accounts/student_batch_result.html', {'users': created_users})

    else:
        # 　初回アクセス時は空のフォームを表示
        form = StudentBatchCreateForm()

    # 　フォーム画面を表示
    return render(request, 'accounts/student_batch_create.html', {'form': form})
