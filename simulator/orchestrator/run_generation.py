from simulator.subscription.generate_plans import generate as generate_plans

from simulator.account.generate_accounts import generate as generate_accounts
from simulator.account.generate_profiles import generate as generate_profiles

from simulator.content.generate_titles import generate as generate_titles
from simulator.content.generate_seasons import generate as generate_seasons
from simulator.content.generate_episodes import generate as generate_episodes
from simulator.subscription.generate_subscriptions import generate as generate_subscriptions
from simulator.payment.generate_invoices import generate as generate_invoices
from simulator.payment.generate_payments import generate as generate_payments

from simulator.playback.generate_playback_events import generate as generate_playback_events
from simulator.playback.generate_search_events import generate as generate_search_events
from simulator.playback.generate_recommendation_events import generate as generate_recommendation_events

def run():

    generate_plans()

    generate_accounts()
    generate_profiles()

    generate_titles()
    generate_seasons()
    generate_episodes()

    generate_subscriptions()
    generate_invoices()
    generate_payments()

    generate_playback_events()
    generate_search_events()
    generate_recommendation_events()

    print("Generation completed")


if __name__ == "__main__":
    run()