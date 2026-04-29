import random
import string
import datetime
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionSubmitChamado(Action):
    """Processa o formulário e gera número de chamado."""

    def name(self) -> Text:
        return "action_submit_chamado"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("user_name") or "Não informado"
        matricula = tracker.get_slot("user_matricula") or "Não informado"
        problema = tracker.get_slot("problema_descricao") or "Não informado"

        # Gera número de chamado único
        ticket = "TI-" + "".join(random.choices(string.digits, k=6))
        now = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M")

        dispatcher.utter_message(text=(
            f"✅ **Chamado aberto com sucesso!**\n\n"
            f"🎫 **Número do chamado:** `{ticket}`\n"
            f"📅 **Data/Hora:** {now}\n"
            f"👤 **Nome:** {name}\n"
            f"🎓 **Matrícula:** {matricula}\n"
            f"📋 **Problema relatado:**\n> {problema}\n\n"
            f"📧 Você receberá atualizações no e-mail institucional.\n"
            f"⏱️ Prazo de resposta: até **2 dias úteis**.\n\n"
            f"💡 Guarde o número `{ticket}` para acompanhamento em:\n"
            f"🌐 suporte.universidade.edu.br"
        ))

        return [SlotSet("ticket_number", ticket)]


class ActionCheckSystemStatus(Action):
    """Retorna o status simulado dos sistemas universitários."""

    def name(self) -> Text:
        return "action_check_system_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # Simulação de status dos sistemas
        # Em produção, aqui seria feita uma requisição HTTP real à API de monitoramento
        systems = {
            "🌐 Portal do Aluno":          random.choices(["🟢 Online", "🟡 Lento"], weights=[85, 15])[0],
            "📚 Moodle / AVA":             random.choices(["🟢 Online", "🟡 Lento", "🔴 Offline"], weights=[80, 15, 5])[0],
            "📧 E-mail Institucional":     "🟢 Online",
            "🎓 Sistema de Matrícula":     random.choices(["🟢 Online", "🟡 Lento", "🔴 Offline"], weights=[75, 20, 5])[0],
            "🔒 VPN Institucional":        random.choices(["🟢 Online", "🟡 Lento"], weights=[90, 10])[0],
            "☁️ OneDrive / Nuvem":         "🟢 Online",
            "🖨️ Portal de Impressão":      random.choices(["🟢 Online", "🟡 Lento"], weights=[88, 12])[0],
            "🎥 Microsoft Teams":          "🟢 Online",
            "🖥️ Acesso Remoto (RDP)":      random.choices(["🟢 Online", "🟡 Lento"], weights=[80, 20])[0],
        }

        now = datetime.datetime.now().strftime("%H:%M")
        lines = [f"📊 **Status dos Sistemas — {now}**\n"]

        all_ok = True
        for system, status in systems.items():
            lines.append(f"{system}: {status}")
            if "🔴" in status or "🟡" in status:
                all_ok = False

        if all_ok:
            lines.append("\n✅ **Todos os sistemas operacionais!**")
        else:
            lines.append("\n⚠️ Alguns sistemas com instabilidade. Se persistir: 📞 (11) 3333-4444")

        lines.append("\n🔄 Dados atualizados em tempo real via monitoramento TI.")

        dispatcher.utter_message(text="\n".join(lines))
        return []
