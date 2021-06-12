# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\n✅ Send me /help for more info."
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome back to {PROJECT_NAME}

⚪️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Setting up**

1) Đặt bot làm quản trị viên (Nhóm và trong kênh nếu sử dụng cplay)
2) Bắt đầu trò chuyện thoại (voice chat)
3) Thử /play [tên bài hát] bởi quản trị viên lần đầu tiên
*) Nếu userbot đã tham gia, hãy thưởng thức âm nhạc, Nếu không, hãy thêm @{ASSISTANT_NAME} vào nhóm của bạn và thử lại

**Đối với kênh phát nhạc**
1) Đặt tôi làm quản trị viên kênh của bạn
2) Gửi /userbotjoinchannel trong nhóm được liên kết
3) Bây giờ gửi lệnh trong nhóm được liên kết

**Commands**

**=>> Song Playing 🎧**

- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback ⏯**

- /player: Open Settings menu of player
** = >> Phát bài hát 🎧**

- `/play` : Phát bài hát được yêu cầu
- `/play [yt url]` : Phát url yt đã cho
- `/play [âm thanh trả lời]` : Phát âm thanh đã trả lời
- `/dplay` : Phát bài hát qua deezer
- `/splay` : Phát bài hát qua jio saavn
- `/ytplay` : Phát trực tiếp bài hát qua Youtube Music

**=>> Phát lại ⏯**

- `/player` : Mở menu Cài đặt của trình phát
- `/skip` : Bỏ qua bản nhạc hiện tại
- `/pause` : Tạm dừng bản nhạc
- `/resume` : Tiếp tục bản nhạc đã tạm dừng
- `/end` : Dừng phát lại phương tiện
- `/current` : Hiển thị bản nhạc Đang phát hiện tại
- `/playlist` : Hiển thị danh sách phát

*Cmd trình phát và tất cả cmd khác ngoại trừ /play, /current và /playlist chỉ dành cho quản trị viên của nhóm.
""",
        
f"""
**=>> Kênh Chơi Nhạc 🛠 **

⚪️ Chỉ dành cho quản trị viên nhóm được liên kết:

- `/cplay [tên bài hát]` - phát bài hát bạn yêu cầu
- `/cdplay [tên bài hát]` - phát bài hát bạn yêu cầu qua deezer
- `/csplay [tên bài hát]` - phát bài hát bạn yêu cầu qua jio saavn
- `/cplaylist` - Hiển thị danh sách đang phát
- `/cccurrent` - Hiện đang phát
- `/cplayer` - mở bảng cài đặt trình phát nhạc
- `/cpause` - tạm dừng phát bài hát
- `/cresume` - tiếp tục phát bài hát
- `/cskip` - phát bài hát tiếp theo
- `/cend` - dừng phát nhạc
- `/userbotjoinchannel` - mời trợ lý vào cuộc trò chuyện của bạn

kênh cũng có thể được sử dụng `c` ( `/cplay` = `/channelplay` )

⚪️ Nếu bạn không muốn chơi trong nhóm được liên kết:

1) Nhận ID kênh của bạn.
2) Tạo nhóm với tên `Channel Music: your_channel_id`
3) Thêm bot làm quản trị viên Kênh với đầy đủ các quyền
4) Thêm @{ASSISTANT_NAME} vào kênh với tư cách quản trị viên.
5) Đơn giản chỉ cần gửi lệnh trong nhóm của bạn.
""",

f"""
** =>> Các công cụ khác 🧑‍🔧**

- `/musicplayer [on/off]` : Bật/Tắt Trình phát nhạc
- `/admincache` : Cập nhật thông tin quản trị viên của nhóm của bạn. Hãy thử nếu bot không nhận ra quản trị viên
- `/userbotjoin` : Mời @{ASSISTANT_NAME} Userbot tham gia cuộc trò chuyện của bạn

**=>> Lệnh cho người dùng Sudo ⚔️**

 - `/userbotleaveall` - xóa trợ lý khỏi tất cả các cuộc trò chuyện
 - `/ib <trả lời tin nhắn>` - tin nhắn đã trả lời brodcast trên toàn cầu cho tất cả các cuộc trò chuyện
 - `/pmpermit [on/off]` - bật/tắt thông báo pmpermit
*Người dùng Sudo có thể thực hiện bất kỳ lệnh nào trong bất kỳ nhóm nào

"""
      ]
