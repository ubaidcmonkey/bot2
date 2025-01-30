import discord

async def create_ticket(interaction: discord.Interaction, category_name: str):
    guild = interaction.guild
    category = discord.utils.get(guild.categories, name=category_name)

    if not category:
        await interaction.response.send_message("Category not found.", ephemeral=True)
        return

    ticket_channel = await guild.create_text_channel(name=f"ticket-{interaction.user.name}", category=category)
    await interaction.response.send_message(f"Ticket created: {ticket_channel.mention}", ephemeral=True)
