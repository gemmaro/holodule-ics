# Holodule iCalendar

Holodule iCalendarは、[ホロジュール](https://schedule.hololive.tv/)（ホロライ
ブの配信予定）からiCalendarファイル（拡張子は`.ics`）を生成配信するプログラム
です。このファイル形式は、多くのカレンダーアプリ等に登録できます。

![holodule](https://user-images.githubusercontent.com/33576079/76172492-00a80e80-61da-11ea-9590-a6bcc4a4982d.png)

## URL一覧

* [全体](https://gemmaro.github.io/holodule-ics/holodule-all.ics)
* [ホロライブ](https://gemmaro.github.io/holodule-ics/holodule-hololive.ics)
* [ホロスターズ](https://gemmaro.github.io/holodule-ics/holodule-holostars.ics)
* [hololive Indonesia](https://gemmaro.github.io/holodule-ics/holodule-indonesia.ics)
* [hololive English](https://gemmaro.github.io/holodule-ics/holodule-english.ics)
* [HOLOSTARS English](https://gemmaro.github.io/holodule-ics/holodule-holostars_english.ics)
* [hololive DEV\_IS](https://gemmaro.github.io/holodule-ics/holodule-dev_is.ics)

## 設定例

※操作方法はOSのバージョンにより異なる可能性があります。

### iOS (iPhone/iPad)

* ホーム画面の「設定」を開く
* 「パスワードとアカウント」→「アカウントを追加」
* 一番下の「その他」
* 一番下の「照会するカレンダーを追加」
* URL を貼り付けて「次へ」
* そのまま右上の「保存」

### Google Calendar (PC)

* 「設定」を開く
* 左側メニュー「カレンダーの追加」→「URL で追加」
* URL を貼り付け
* 「カレンダーを追加」

PC から追加後はモバイル版 Google Calendar でも閲覧できます。

## 雑記

### カレンダーの更新頻度

1時間に1回としています（ホロジュールは15分に1度のようです）。

カレンダーアプリの更新頻度により、カレンダーへの反映が遅くなる可能性があります。
iOS では、設定より更新頻度を設定できます。

### 通知が欲しい

カレンダー側で通知を設定できるものがあります。
[ホロプラス](https://www.holoplus.com/)、YouTubeチャンネルの通知機能等もご検討ください。

### 配信の長さについて

配信の長さは全て **2時間** に固定しています。
ホロジュールでは、配信開始の予定時間のみが得られるためです。

### 配信のサイト

YouTube以外の配信予定はカレンダーファイルに生成されないことがあります。
例えばTwitchやAbemaが該当します。

## バグ・要望

* [機能の要望など](https://github.com/gemmaro/holodule-ics/discussions)
* [不具合の報告など](https://github.com/gemmaro/holodule-ics/issues)

## 謝辞

このプログラムは[sarisia/holodule-ics](https://github.com/sarisia/holodule-ics)を元にしています。

## 使用許諾

このプログラムの開発、運用は[ホロライブプロダクションの二次創作ガイドライン](https://hololivepro.com/terms/ "hololive")に則って行います。

このプログラムはMITライセンスの元に配布されます。
詳細は[LICENSEファイル](LICENSE)をご参照ください。
