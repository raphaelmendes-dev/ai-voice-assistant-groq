"""
Text-to-Speech - Integração com gTTS (Google)
==============================================
Síntese de fala a partir de texto com suporte multilíngue.

Dependencies:
    - gtts: Google Text-to-Speech
"""

import os
import tempfile
from pathlib import Path
from typing import Optional

from gtts import gTTS


class TTSEngine:
    """
    Engine de text-to-speech usando Google TTS.
    
    Características:
        - Suporte a 100+ idiomas
        - Voz natural do Google
        - Rápido e gratuito
        - Ajuste de velocidade
    
    Attributes:
        temp_dir: Diretório para arquivos temporários
        default_language: Idioma padrão se não especificado
        slow_speed: Usar velocidade reduzida
    """
    
    DEFAULT_LANGUAGE = "pt"  # Português como padrão
    
    def __init__(self, slow_speed: bool = False):
        """
        Inicializa o engine TTS.
        
        Args:
            slow_speed: Se True, usa velocidade de fala reduzida
        """
        self.temp_dir = Path(tempfile.gettempdir()) / "voice_assistant"
        self.temp_dir.mkdir(exist_ok=True)
        self.default_language = self.DEFAULT_LANGUAGE
        self.slow_speed = slow_speed
    
    def _get_temp_audio_file(self) -> str:
        """
        Gera caminho para arquivo de áudio temporário.
        
        Returns:
            Caminho completo do arquivo temporário
        """
        return str(self.temp_dir / f"output_{os.getpid()}.mp3")
    
    def _normalize_language_code(self, language: str) -> str:
        """
        Normaliza código de idioma para formato do gTTS.
        
        Args:
            language: Código de idioma (ex: 'pt', 'en', 'es')
            
        Returns:
            Código normalizado
        """
        # Mapeamento de códigos comuns
        lang_mapping = {
            "pt": "pt",      # Português
            "pt-br": "pt",   # Português brasileiro
            "pt-pt": "pt",   # Português europeu
            "en": "en",      # Inglês
            "es": "es",      # Espanhol
            "fr": "fr",      # Francês
            "de": "de",      # Alemão
            "it": "it",      # Italiano
            "zh": "zh-CN",   # Chinês simplificado
            "ja": "ja",      # Japonês
            "ko": "ko",      # Coreano
            "ru": "ru",      # Russo
            "ar": "ar",      # Árabe
            "hi": "hi",      # Hindi
            "nl": "nl",      # Holandês
            "pl": "pl",      # Polonês
            "tr": "tr",      # Turco
            "sv": "sv",      # Sueco
            "da": "da",      # Dinamarquês
            "fi": "fi",      # Finlandês
            "no": "no",      # Norueguês
            "uk": "uk",      # Ucraniano
        }
        
        return lang_mapping.get(language.lower(), self.default_language)
    
    def synthesize(
        self, 
        text: str,
        language: Optional[str] = None,
        slow: Optional[bool] = None
    ) -> Optional[str]:
        """
        Sintetiza texto em áudio.
        
        Args:
            text: Texto a ser sintetizado
            language: Código do idioma (usa padrão se None)
            slow: Velocidade reduzida (usa configuração da classe se None)
            
        Returns:
            Caminho do arquivo de áudio gerado ou None em caso de erro
        """
        if not text or not text.strip():
            print("⚠️  Texto vazio, não há nada para sintetizar.")
            return None
        
        # Preparar parâmetros
        lang = self._normalize_language_code(language or self.default_language)
        use_slow = slow if slow is not None else self.slow_speed
        
        try:
            # Criar objeto TTS
            tts = gTTS(
                text=text,
                lang=lang,
                slow=use_slow
            )
            
            # Salvar arquivo de áudio
            output_file = self._get_temp_audio_file()
            tts.save(output_file)
            
            return output_file
            
        except Exception as e:
            print(f"❌ Erro na síntese de voz: {e}")
            return None
    
    def synthesize_with_breaks(
        self, 
        text: str,
        language: Optional[str] = None,
        break_duration: float = 0.5
    ) -> Optional[str]:
        """
        Sintetiza texto com pausas entre frases.
        
        Args:
            text: Texto a ser sintetizado
            language: Código do idioma
            break_duration: Duração da pausa em segundos
            
        Returns:
            Caminho do arquivo de áudio gerado
        """
        # Para gTTS simples, apenas adiciona pontuação para pausas naturais
        enhanced_text = text.replace(". ", "... ")
        enhanced_text = enhanced_text.replace("! ", "!... ")
        enhanced_text = enhanced_text.replace("? ", "?... ")
        
        return self.synthesize(enhanced_text, language)
    
    def get_supported_languages(self) -> dict:
        """
        Retorna dicionário de idiomas suportados.
        
        Returns:
            Dict com código e nome do idioma
        """
        return {
            "pt": "Português",
            "en": "English",
            "es": "Español",
            "fr": "Français",
            "de": "Deutsch",
            "it": "Italiano",
            "zh-CN": "中文",
            "ja": "日本語",
            "ko": "한국어",
            "ru": "Русский",
            "ar": "العربية",
            "hi": "हिन्दी",
            "nl": "Nederlands",
            "pl": "Polski",
            "tr": "Türkçe",
            "sv": "Svenska",
            "da": "Dansk",
            "fi": "Suomi",
            "no": "Norsk",
            "uk": "Українська"
        }
    
    def test_synthesis(self, language: str = "pt") -> bool:
        """
        Testa se a síntese está funcionando.
        
        Args:
            language: Código do idioma para testar
            
        Returns:
            True se teste passou, False caso contrário
        """
        test_texts = {
            "pt": "Olá! Este é um teste de síntese de voz.",
            "en": "Hello! This is a voice synthesis test.",
            "es": "¡Hola! Esta es una prueba de síntesis de voz.",
            "fr": "Bonjour! Ceci est un test de synthèse vocale.",
            "de": "Hallo! Dies ist ein Sprachsynthesetest."
        }
        
        test_text = test_texts.get(language, test_texts["pt"])
        
        try:
            result = self.synthesize(test_text, language)
            
            if result and os.path.exists(result):
                print(f"✅ Teste de síntese bem-sucedido ({language})")
                
                # Limpar arquivo de teste
                try:
                    os.remove(result)
                except:
                    pass
                
                return True
            else:
                print(f"❌ Teste de síntese falhou ({language})")
                return False
                
        except Exception as e:
            print(f"❌ Erro no teste de síntese: {e}")
            return False
    
    def cleanup_temp_files(self) -> None:
        """Remove arquivos temporários de áudio."""
        try:
            for file in self.temp_dir.glob("output_*.mp3"):
                file.unlink()
            print("🧹 Arquivos temporários de TTS removidos.")
        except Exception as e:
            print(f"⚠️  Erro ao limpar arquivos temporários: {e}")
    
    def __del__(self):
        """Limpa recursos ao destruir objeto."""
        try:
            self.cleanup_temp_files()
        except:
            pass
