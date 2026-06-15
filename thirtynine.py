import matplotlib.pyplot as plt

# Who wins more on value for money?
platforms = ['Daraz', 'OLX']
vfm_wins  = [4, 1]   # from our Day 8 report

fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 3 charts side by side

# Chart 1 — Cheaper platform wins
axes[0].pie([3, 2], labels=['OLX', 'Daraz'], autopct='%1.1f%%',
            colors=['orange', 'blue'])
axes[0].set_title('Cheaper Platform')

# Chart 2 — Better rated wins
axes[1].pie([5, 0], labels=['Daraz', 'OLX'], autopct='%1.1f%%',
            colors=['blue', 'orange'])
axes[1].set_title('Better Rated')

# Chart 3 — Better VFM wins
axes[2].pie([4, 1], labels=['Daraz', 'OLX'], autopct='%1.1f%%',
            colors=['blue', 'orange'])
axes[2].set_title('Better Value (VFM)')

plt.suptitle('Daraz vs OLX -- Overall Winner Analysis', fontsize=14)
plt.tight_layout()
plt.show()