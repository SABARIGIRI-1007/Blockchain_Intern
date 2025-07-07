import random

# ------------------- Proof of Work (PoW) -------------------
miner = {
    "id": "Miner1",
    "power": random.randint(1, 100)
}
print("=== Proof of Work (PoW) ===")
print(f"Selected validator: {miner['id']}")
print(f"Power assigned: {miner['power']}")
print()

# ------------------- Proof of Stake (PoS) -------------------
staker = {
    "id": "Staker1",
    "stake": random.randint(1, 100)
}
print("=== Proof of Stake (PoS) ===")
print(f"Selected validator: {staker['id']}")
print(f"Stake held: {staker['stake']}")
print()

# ---------------- Delegated Proof of Stake (DPoS) ----------------
voters = ["A", "B", "C"]
delegates = ["Del1", "Del2", "Del3"]
votes = {d: 0 for d in delegates}

for voter in voters:
    vote = random.choice(delegates)
    votes[vote] += 1
    print(f"Voter {voter} voted for {vote}")

selected = max(votes, key=votes.get)
print("\n=== Delegated Proof of Stake (DPoS) ===")
print("Vote count:", votes)
print(f"Selected delegate: {selected} with {votes[selected]} votes")
