from ..types import Types

#parse (remember to do static methods, unless you're changing the formatting)
class StartParse(object): #really hope this doesn't take too long to run...
	@staticmethod
	def ready(response):
		data = response.get("d", {})
		ready_data = dict(data)
		ready_data.pop("merged_members", None)
		users = data.get("users", [])
		user_pool = {h.get("id"): h for h in users if isinstance(h, dict) and h.get("id")}
		relationships = data.get("relationships", [])
		ready_data["relationships"] = {}
		for i in relationships:
			if not isinstance(i, dict):
				continue
			rel_id = i.get("id")
			rel_type = Types.relationshipTypes.get(i.get("type"), i.get("type"))
			if rel_id:
				ready_data["relationships"][rel_id] = dict(dict(i, **{"type": rel_type}), **user_pool.get(rel_id, {}))
		ready_data["private_channels"] = {}
		for j in data.get("private_channels", []):
			if not isinstance(j, dict):
				continue
			channel_id = j.get("id")
			if not channel_id:
				continue
			channel_type = Types.channelTypes.get(j.get("type"), j.get("type"))
			ready_data["private_channels"][channel_id] = dict(j, **{"type": channel_type})
			if "recipient_ids" in ready_data["private_channels"][channel_id]:
				recipient_ids = ready_data["private_channels"][channel_id].pop("recipient_ids", [])
				ready_data["private_channels"][channel_id]["recipients"] = {
					q: user_pool.get(q, {}) for q in recipient_ids
				}
		ready_data.setdefault("user_settings", {})
		ready_data["user_settings"].setdefault("activities", {})
		guilds = data.get("guilds", [])
		ready_data["guilds"] = {k.get("id"): k for k in guilds if isinstance(k, dict) and k.get("id")}
		current_user_id = data.get("user", {}).get("id")
		merged_members = data.get("merged_members", [])
		for personal_role, guild in zip(merged_members, guilds):
			if not isinstance(guild, dict):
				continue
			guild_id = guild.get("id")
			if not guild_id or guild_id not in ready_data["guilds"]:
				continue
			if "unavailable" not in ready_data["guilds"][guild_id]:
				if isinstance(guild.get("emojis"), list):
					ready_data["guilds"][guild_id]["emojis"] = {
						l.get("id"): l for l in guild["emojis"] if isinstance(l, dict) and l.get("id")
					}
				if isinstance(guild.get("roles"), list):
					ready_data["guilds"][guild_id]["roles"] = {
						m.get("id"): m for m in guild["roles"] if isinstance(m, dict) and m.get("id")
					}
				if isinstance(guild.get("channels"), list):
					ready_data["guilds"][guild_id]["channels"] = {
						n.get("id"): dict(n, **{"type": Types.channelTypes.get(n.get("type"), n.get("type"))})
						for n in guild["channels"]
						if isinstance(n, dict) and n.get("id")
					}
			if isinstance(personal_role, list) and current_user_id:
				ready_data["guilds"][guild_id]["my_data"] = next(
					(i for i in personal_role if isinstance(i, dict) and i.get("user_id") == current_user_id),
					{}
				)
			else:
				ready_data["guilds"][guild_id]["my_data"] = {}
			ready_data["guilds"][guild_id]["members"] = {}
		return ready_data

	@staticmethod
	def ready_supplemental(response):
		data = response.get("d", {})
		ready_supp_data = dict(data)
		merged_presences = data.get("merged_presences", {})
		friends = merged_presences.get("friends", [])
		ready_supp_data["online_friends"] = {
			o.get("user_id"): o for o in friends
			if isinstance(o, dict) and o.get("user_id")
		}
		ready_supp_data.pop("guilds", None)
		ready_supp_data["voice_states"] = {
			p.get("id"): p.get("voice_states", [])
			for p in data.get("guilds", [])
			if isinstance(p, dict) and p.get("id")
		}
		return ready_supp_data
