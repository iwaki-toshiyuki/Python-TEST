from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Baseクラスの作成
Base = declarative_base()

# データベースエンジンの作成（SQLiteを使用）
engine = create_engine('sqlite:///users.db', echo=True)

# Userクラスの定義
class User(Base):
    # テーブル名を指定
    __tablename__ = "users"
    # idカラムの定義
    user_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    # 名前カラムの定義（重複禁止）
    name = Column(String(255),unique=False)
    # 職業カラムの定義
    job = Column(String(50))
    
# テーブルの作成
Base.metadata.create_all(engine)

# セッションの作成
Session = sessionmaker(bind=engine)
session = Session()

# Read（読み込み）関数
def display_users(session):
    """現在のユーザーを表示する関数"""
    users = session.query(User).all()
    print("現在のユーザー:")
    for user in users:
        print(f"名前: {user.name}, 職業: {user.job}")

# Create（作成）関数
def add_user():
    """ユーザーを追加する関数"""
    name = input("追加するユーザーの名前を入力してください: ")
    
    # 重複チェック
    existing_user = session.query(User).filter_by(name=name).first()
    if existing_user:
        print(f"ユーザー {name} は既に存在します。別の名前を入力してください。")
        return
    
    job = input("追加するユーザーの職業を入力してください: ")
    new_user = User(name=name, job=job)
    session.add(new_user)
    session.commit()
    print(f"ユーザー {name} が追加されました。")
    display_users(session)
    
# Update（更新）関数   
def update_user():
    """ユーザーの職業を更新する関数"""
    name = input("更新するユーザーの名前を入力してください: ")
    job = input("新しい職業を入力してください: ")
    
    user = session.query(User).filter_by(name=name).first()
    
    if user:
        user.job = job
        session.commit()
        print(f"{name} の職業が {job} に更新されました。")
    else:
        print(f"ユーザー {name} は見つかりませんでした。")
    display_users(session)
    
# Delete（削除）関数
def delete_user():
    """ユーザーを削除する関数"""
    name = input("削除するユーザーの名前を入力してください: ")

    user = session.query(User).filter_by(name=name).first()
    
    
    if user:
        session.delete(user)
        session.commit()
        print(f"ユーザー {name} が削除されました。")
    else:
        print(f"ユーザー {name} は見つかりませんでした。")
    display_users(session)
    
    
def main():
    """操作を選択するメイン関数"""
    while True:
        print("\n操作を選択してください:")
        print("1: ユーザーを追加")
        print("2: ユーザー情報の更新")
        print("3: ユーザーの削除")
        print("4: 現在のユーザーを表示")
        print("5: 終了")
        choice = input("選択肢（1-5）: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            update_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            display_users(session)
        elif choice == '5':
            print("終了します。")
            break
        else:
            print("無効な選択肢です。もう一度お試しください。")

if __name__ == "__main__":
    main()