class ResearchAgent:
    def analyze_startup(self, startup_name):
        return {
            "domain": "Technology / Consumer Services",
            "growth_signal": f"{startup_name} is operating in a rapidly expanding market.",
            "risk_factor": "High competition and funding dependency."
        }


class MarketAgent:
    def analyze_market(self, startup_name):
        return {
            "competition_level": "Moderate to High",
            "market_trend": "Increasing digital adoption",
            "opportunity": f"{startup_name} can expand into Tier-2 and Tier-3 markets."
        }


class StrategyAgent:
    def suggest_strategy(self, startup_name):
        return {
            "pricing_strategy": "Introduce premium tier features",
            "retention_strategy": "Improve customer engagement through loyalty programs",
            "expansion_strategy": "Strategic partnerships and ecosystem integration"
        }


class CoordinatorAgent:
    def __init__(self):
        self.research = ResearchAgent()
        self.market = MarketAgent()
        self.strategy = StrategyAgent()

    def run_analysis(self, startup_name):
        research_data = self.research.analyze_startup(startup_name)
        market_data = self.market.analyze_market(startup_name)
        strategy_data = self.strategy.suggest_strategy(startup_name)

        report = {
            "Startup": startup_name,
            "Research Insights": research_data,
            "Market Insights": market_data,
            "Strategic Recommendations": strategy_data
        }

        return report