from config.constants.settings import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_IDS,
    TEAMS_CONVERSATION_IDS,
    SLACK_CHANNEL_ID,
    SLACK_BOT_TOKEN
)
from src.utils.core import (
    get_logger,
    log_exceptions,
    NotificationException,
    ExtractTestCaseFailed,
    TC_NAME
)
from slack_sdk import WebClient

logger = get_logger(__name__)

class ReportMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="INFO")
    def prepare_message(self):
        try:
            logger.debug("Preparing test report message")
            logger.debug(f"TC_NAME contains {len(TC_NAME)} failures: {TC_NAME}")
            
            unique_failures = list(dict.fromkeys(TC_NAME))
            logger.debug(f"Unique failures after deduplication: {len(unique_failures)} items: {unique_failures}")
            
            from datetime import datetime
            now = datetime.now()
            timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
            
            txt = f"AFFILIATE 12BET AUTOMATION REPORT\n"
            txt += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            txt += f"📅 Date: {timestamp}\n"
            
            func_name = getattr(self, 'FuncName', 'Unknown Test Suite')
            env = getattr(self, 'env', 'unknown')
            
            txt += f"📋 Test Suite: {func_name}\n"
            txt += f"🌐 Environment: {env.upper()}\n"
            
            if bool(unique_failures):
                failure_count = len(unique_failures)
                txt += f"⚠️ Status: FAILED ({failure_count} test cases)\n"
                txt += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                txt += f"❌ Failed Test Cases:\n"
                
                for idx, tc in enumerate(unique_failures, 1):
                    txt += f"{idx}. {str(tc).replace('_', ' ')}\n"
            else:
                txt += f"✅ Status: PASSED (All test cases)\n"
            
            txt += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            logger.debug(f"Generated report message successfully")
            return txt
        except Exception as e:
            logger.error(f"Error preparing message: {str(e)}")
            return f"⚠️ ERROR IN TEST REPORT ⚠️\nError details: {str(e)}"

    @log_exceptions(log_level="INFO")
    def send_message_to_telegram(self):
        try:
            TOKEN = TELEGRAM_BOT_TOKEN
            if TOKEN == "":
                logger.debug("Telegram bot token not set, skipping message")
                return
                
            logger.info("Sending test report to Telegram")
            bot_message = self.prepare_message()
            chat_ids = TELEGRAM_CHAT_IDS
            
            for id in chat_ids:
                url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                obj = {
                    "chat_id": id,
                    "parse_mode": "Markdown",
                    "text": bot_message
                }
                logger.debug(f"Sending message to Telegram chat ID: {id}")
                self.api.post(url=url, data=obj)
                
            logger.info(f"Test report sent to {len(chat_ids)} Telegram chats")
        except Exception as e:
            logger.error(f"Failed to send message to Telegram: {str(e)}")
            raise NotificationException(
                message="Failed to send message to Telegram",
                channel="Telegram",
                details=str(e)
            )

    @log_exceptions(log_level="INFO")
    def send_message_to_team(self):
        try:
            conversationId = TEAMS_CONVERSATION_IDS
            if len(conversationId) == 0:
                logger.debug("MS Teams conversation IDs not set, skipping message")
                return
                
            logger.info("Sending test report to MS Teams")
            bot_message = self.prepare_message()           
            
            url = "https://api-fanexbot.nexdev.net/api/msteams/send"
            sent_count = 0
            
            for id in conversationId:
                obj = {
                    "appId": 1021,
                    "conversationId": id,
                    "Content": bot_message
                }
                logger.debug(f"Sending message to Teams conversation ID: {id}")
                self.api.post(url=url, formData=obj)
                sent_count += 1
                
            logger.info(f"Test report sent to {sent_count} MS Teams conversations")
        except Exception as e:
            logger.error(f"Failed to send message to MS Teams: {str(e)}")
            raise NotificationException(
                message="Failed to send message to MS Teams",
                channel="MS Teams",
                details=str(e)
            )

    @log_exceptions(log_level="INFO")
    def send_message_to_slack(self):
        try:
            channel_id = SLACK_CHANNEL_ID
            if not channel_id:
                logger.debug("Slack channel ID not set, skipping message")
                return
            
            logger.info("Sending test report to Slack")
            bot_message = self.prepare_message()

            client = WebClient(token=SLACK_BOT_TOKEN)
            send_count = 0

            for id in channel_id:
                try:
                    logger.debug(f"Sending message to Slack channel {id}")
                    client.chat_postMessage(channel=id, text=bot_message)
                    send_count += 1
                except Exception as e:
                    logger.error(f"Failed to send message to Slack channel {id}: {str(e)}")
                    
            logger.info(f"Test report sent to {send_count} Slack channels")

        except Exception as e:
            logger.error(f"Failed to send message to Slack: {str(e)}")
            raise NotificationException(
                message="Failed to send message to Slack",
                channel="Slack",
                details=str(e)
            )