from enum import IntEnum, IntFlag
from attrs import define, field
from retux.client.resources.abc import Snowflake, Object, Partial
from retux.client.resources.user import User

__all__ = (
    "Channel",
    "FollowedChannel",
    "MessageActivity",
    "ChannelType",
    "ChannelFlags",
    "MessageType",
    "MessageActivityType",
    "MessageFlags",
    "VideoQualityMode",
    "Overwrite",
)


class ChannelType(IntEnum):
    """
    Represents the types of channels from Discord

    Constants
    ---------
    GUILD_TEXT
        A text channel within a server.
    DM
        A direct message between users.
    GUILD_VOICE
        A voice channel within a server.
    GROUP_DM
        A direct message between multiple users.
    GUILD_CATEGORY
        An organizational category that contains up to 50 channels.
    GUILD_NEWS
        A channel that users can follow and crosspost into their own server.
    GUILD_NEWS_THREAD
        A temporary sub-channel within a GUILD_NEWS channel.
    GUILD_PUBLIC_THREAD
        A temporary sub-channel within a GUILD_TEXT channel.
    GUILD_PRIVATE_THREAD
        A temporary sub-channel within a GUILD_TEXT channel.

        Only viewable by those invited and those with the MANAGE_THREADS permission
    GUILD_STAGE_VOICE
        A voice channel for hosting events with an audience.
    GUILD_DIRECTORY
        The channel in a hub containing the listed servers.
    GUILD_FORUM
        A channel that can only contain threads.
    """

    GUILD_TEXT = 0
    """A text channel within a server."""
    DM = 1
    """A direct message between users."""
    GUILD_VOICE = 2
    """A voice channel within a server."""
    GROUP_DM = 3
    """A direct message between multiple users."""
    GUILD_CATEGORY = 4
    """An organizational category that contains up to 50 channels."""
    GUILD_NEWS = 5
    """A channel that users can follow and crosspost into their own server."""
    GUILD_NEWS_THREAD = 10
    """A temporary sub-channel within a GUILD_NEWS channel."""
    GUILD_PUBLIC_THREAD = 11
    """A temporary sub-channel within a GUILD_TEXT channel."""
    GUILD_PRIVATE_THREAD = 12
    """
    A temporary sub-channel within a GUILD_TEXT channel.

    Only viewable by those invited and those with the MANAGE_THREADS permission
    """
    GUILD_STAGE_VOICE = 13
    """A voice channel for hosting events with an audience."""
    GUILD_DIRECTORY = 14
    """The channel in a hub containing the listed servers."""
    GUILD_FORUM = 15
    """A channel that can only contain threads."""


class VideoQualityMode(IntEnum):
    """
    Represents video quality modes from Discord

    Constants
    ---------
    AUTO
        Discord chooses the quality for optimal performance.
    FULL
        720p video resolution (1280x720).
    """

    AUTO = 1
    """Discord chooses the quality for optimal performance."""
    FULL = 2
    """720p video resolution (1280x720)."""


class ChannelFlags(IntFlag):
    """The bitwise values that represent channel flags from Discord"""

    PINNED = 1 << 1
    """
    This thread is pinned to the top of its parent channel.

    Only available on forum channels.
    """


class MessageType(IntEnum):
    """
    Represnts message types from Discord

    Constants
    ---------
    DEFAULT
        A normal message.
    RECIPIENT_ADD
        Unknown
    RECIPIENT_REMOVE
        Unknown
    CALL
        An indicator for a new voice call in a DM.
    CHANNEL_NAME_CHANGE
        A notification message for name of a channel changing.
    CHANNEL_ICON_CHANGE
        A notification message for the icon of a DM changing.
    CHANNEL_PINNED_MESSAGE
        A notification message for a new pinned message.
    USER_JOIN
        A notification message about the name of a channel changing.
    GUILD_BOOST
        A notification message about a new server boost(s).
    GUILD_BOOST_TIER_1
        A notification message about a guild reaching level 1 boost perks.
    GUILD_BOOST_TIER_2
        A notification message about a guild reaching level 2 boost perks.
    GUILD_BOOST_TIER_3
        A notification message about a guild reaching level 3 boost perks.
    CHANNEL_FOLLOW_ADD
        A notification message about a new follower of a news channel.
    GUILD_DISCOVERY_DISQUALIFIED
        A notification message about a guild being disqualified for discovery.
    GUILD_DISCOVERY_REQUALIFIED
        A notification message about a guild being requalified for discovery.
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING
        An intial warning for a discovery grace period.
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING
        A final warning for a discovery grace period.
    THREAD_CREATED
        A notification message for a new thread in a channel.
    REPLY
        A reply to a message.
    CHAT_INPUT_COMMAND
        A resulting message from a slash command being used.
    THREAD_STARTER_MESSAGE
        A starter message for a thread.
    GUILD_INVITE_REMINDER
        A reminder about a guild invite.
    CONTEXT_MENU_COMMAND
        A resulting message from a context menu command being used.
    AUTO_MODERATION_ACTION
        A message from AutoMod describing an action it took.
    """

    DEFAULT = 0
    """A normal message."""
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    """An indicator for a new voice call in a DM."""
    CHANNEL_NAME_CHANGE = 4
    """A notification message for name of a channel changing."""
    CHANNEL_ICON_CHANGE = 5
    """A notification message for the icon of a DM changing."""
    CHANNEL_PINNED_MESSAGE = 6
    """A notification message for a new pinned message."""
    USER_JOIN = 7
    """A notification message about the name of a channel changing."""
    GUILD_BOOST = 8
    """A notification message about a new server boost(s)."""
    GUILD_BOOST_TIER_1 = 9
    """A notification message about a guild reaching level 1 boost perks."""
    GUILD_BOOST_TIER_2 = 10
    """A notification message about a guild reaching level 2 boost perks."""
    GUILD_BOOST_TIER_3 = 11
    """A notification message about a guild reaching level 3 boost perks."""
    CHANNEL_FOLLOW_ADD = 12
    """A notification message about a new follower of a news channel."""
    GUILD_DISCOVERY_DISQUALIFIED = 14
    """A notification message about a guild being disqualified for discovery."""
    GUILD_DISCOVERY_REQUALIFIED = 15
    """A notification message about a guild being requalified for discovery."""
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    """An intial warning for a discovery grace period."""
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    """A final warning for a discovery grace period."""
    THREAD_CREATED = 18
    """A notification message for a new thread in a channel."""
    REPLY = 19
    """A reply to a message."""
    CHAT_INPUT_COMMAND = 20
    """A resulting message from a slash command being used."""
    THREAD_STARTER_MESSAGE = 21
    """A starter message for a thread."""
    GUILD_INVITE_REMINDER = 22
    """A reminder about a guild invite."""
    CONTEXT_MENU_COMMAND = 23
    """A resulting message from a context menu command being used."""
    AUTO_MODERATION_ACTION = 24
    """A message from AutoMod describing an action it took."""


class MessageActivityType(IntEnum):
    """
    Represents a message activity type from Discord.

    Constants
    ---------
    JOIN
        A join message activity.
    SPECTATE
        A spectate message activity.
    LISTEN
        A listen message activity.
    JOIN_REQUEST
        A join request message activity.
    """

    JOIN = 1
    """A join message activity."""
    SPECTATE = 2
    """A spectate message activity."""
    LISTEN = 3
    """A listen message activity."""
    JOIN_REQUEST = 5
    """A join request message activity."""


class MessageFlags(IntFlag):
    """The bitwise values that represent message flags from Discord"""

    CROSSPOSTED = 1 << 0
    """This message has been published to subscribed channels."""
    IS_CROSSPOST = 1 << 1
    """This message originated from a message in another channel."""
    SUPPRESS_EMBEDS = 1 << 2
    """Do not include any embeds when serializing this message."""
    SOURCE_MESSAGE_DELETED = 1 << 3
    """The source message for this crosspost has been deleted."""
    URGENT = 1 << 4
    """This message came from the urgent message system."""
    HAS_THREAD = 1 << 5
    """This message has an associated thread, with the same ID as the message."""
    EPHEMERAL = 1 << 6
    """This message is only visible to the user who invoked the interaction."""
    LOADING = 1 << 7
    """This message is an interaction response showing that the bot is "thinking"."""
    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD = 1 << 8
    """This message failed to mention some roles and add their members to the thread."""


@define()
class Overwrite(Object):
    """
    Represents a permission overwrite from Discord.

    Attributes
    ----------
    id : `Snowflake`
        The ID of the role or user.
    type : `int`
        The type of overwrite.

        Use `0` for to overwrite a role's permission and `1` to overwrite a guild member's permission.
    allow : `str`
        The bit set representing the overwrite's allowed permissions.
    deny : `str`
        The bit set representing the overwrite's denied permissions.
    """

    id: str | Snowflake = field(converter=Snowflake)
    """The ID of the role or user."""
    type: int = field()
    """
    The type of overwrite.

    Use `0` for to overwrite a role's permission and `1` to overwrite a guild member's permission.
    """
    allow: str = field()
    """The bit set representing the overwrite's allowed permissions."""
    deny: str = field()
    """The bit set representing the overwrite's denied permissions."""


@define()
class MessageActivity:
    """
    Represents a message activity structure from Discord.

    Attributes
    ----------
    type : `int`
        The type of message activity.
    party_id : `Snowflake`, optional
        The ID of a party from a rich presence event.
    """

    type: int | MessageActivityType = field(converter=MessageActivityType)
    """The type of message activity."""
    party_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """The ID of a party from a rich presence event."""


@define()
class FollowedChannel:
    """
    Represents a followed channel from Discord.

    Attributes
    ----------
    channel_id : `Snowflake`
        The ID of the source channel.
    webhook_id : `Snowflake`
        The ID of the created target webhook.
    """

    channel_id: str | Snowflake = field(converter=Snowflake)
    """The ID of the source channel."""
    webhook_id: str | Snowflake = field(converter=Snowflake)
    """The ID of the created target webhook."""


@define(kw_only=True)
class TextChannel(Partial, Object):
    """
    Represents a text channel from Discord.

    ---

    This is an event-specific dataclass that is not passed by
    Discord's Gateway. This will only contain the data relevant
    to a text channel -- and just the `id` of it. `type` is
    dropped as this is already given for the event handler via.
    specification in the typehinting.

    ---

    Attributes
    ----------
    id : `Snowflake`
        The ID of the channel.
    guild_id : `Snowflake`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    topic : `str`, optional
        The topic of the channel.

        A channel topic is in-between 1-1024 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `Snowflake`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `Snowflake`, optional
        The ID of the creator of the group dm or thread.
    application_id : `Snowflake`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `Snowflake`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    id: str | Snowflake = field(converter=Snowflake)
    """The ID of the channel."""
    guild_id: str | Snowflake | None = field(default=None, converter=Snowflake)
    """
    The ID of the guild.

    This is nullable due to some Gateway events
    lacking the data for the ID.
    """
    position: int | None = field(default=None)
    """Sorted position of the channel."""
    permission_overwrites: list[dict] | list[Overwrite] | None = field(default=None)
    """Explicit permission overwrites for members and roles."""
    name: str | None = field(default=None)
    """
    The name of the channel.

    A channel name is in-between 1-100 characters.
    """
    topic: str | None = field(default=None)
    """
    The topic of the channel.

    A channel topic is in-between 1-1024 characters.
    """
    nsfw: bool | None = field(default=False)
    """Whether or not the channel is NSFW. Defaults to `False`."""
    last_message_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """
    The ID of the last message sent in this channel.

    Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    """
    rate_limit_per_user: int | None = field(default=None)
    """
    Amount of seconds a user has to wait before sending another message

    Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    """
    recipients: list[dict] | list[User] | None = field(default=None)
    """The recipients of the dm."""
    icon: str | None = field(default=None)
    """The hash for the channel's icon."""
    owner_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """The ID of the creator of the group dm or thread."""
    application_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """The ID of the application that created the dm if it is bot-created."""
    parent_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """
    The ID of the parent of the channel

    Represents the parent category for regular channels and the parent channel for threads.
    """
    last_pin_timestamp: str | None = field(default=None)
    """The time when the last message was pinned."""
    """The video quality mode of the voice channel."""
    message_count: int | None = field(default=None)
    """"
    The approximated amount of messages in a thread.

    Stops counting at `50`.
    """
    member_count: int | None = field(default=None)
    """
    The approximated amount of users in a thread.

    Stops counting at `50`.
    """
    # TODO: implement Thread Metadata object.
    thread_metadata: dict | ThreadMetadata | None = field(  # noqa
        converter=ThreadMetadata, default=None  # noqa
    )  # noqa
    """Thread-specific fields not needed by other channels."""
    # TODO: implement Thread Member object.
    member: dict | ThreadMember | None = field(converter=ThreadMember, default=None)  # noqa
    """
    The thread member representation of the user if they have joined the thread.

    This is only included on certain api endpoints.
    """
    default_auto_archive_duration: int | None = field(default=None)
    """
    The default archive duration for threads in minutes.

    Can be set to `60`, `1440`, `4320`, `10080`.
    """
    permissions: str | None = field(default=None)
    """
    The computed permissions for the invoking user in the channel, including any overwrites.

    Only included when part of the resolved data received on a slash command interaction.
    """
    flags: int | ChannelFlags | None = field(converter=ChannelFlags, default=None)
    """Channel flags combined as a bitfield."""


@define(kw_only=True)
class AnnouncementChannel(TextChannel):
    """
    Represents an announcement channel on Discord.

    ---

    This information is essentially in vogue the same as a
    text channel, presented with the `TextChannel` object.

    ---

    Attributes
    ----------
    id : `Snowflake`
        The ID of the channel.
    guild_id : `Snowflake`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    topic : `str`, optional
        The topic of the channel.

        A channel topic is in-between 1-1024 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `Snowflake`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `Snowflake`, optional
        The ID of the creator of the group dm or thread.
    application_id : `Snowflake`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `Snowflake`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """


@define(kw_only=True)
class ForumChannel(TextChannel):
    """
    Represents a forum channel on Discord.

    ---

    This information is essentially in vogue the same as a
    text channel, presented with the `TextChannel` object.

    ---

    Attributes
    ----------
    id : `Snowflake`
        The ID of the channel.
    guild_id : `Snowflake`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    topic : `str`, optional
        The topic of the channel.

        A channel topic is in-between 1-1024 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `Snowflake`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `Snowflake`, optional
        The ID of the creator of the group dm or thread.
    application_id : `Snowflake`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `Snowflake`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """


@define(kw_only=True)
class DMChannel(TextChannel):
    """
    Represents a DM channel on Discord.

    ---

    This information is essentially in vogue the same as a
    text channel, presented with the `TextChannel` object.

    ---

    Attributes
    ----------
    id : `Snowflake`
        The ID of the channel.
    guild_id : `Snowflake`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    topic : `str`, optional
        The topic of the channel.

        A channel topic is in-between 1-1024 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `Snowflake`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `Snowflake`, optional
        The ID of the creator of the group dm or thread.
    application_id : `Snowflake`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `Snowflake`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """


@define(kw_only=True)
class VoiceChannel(Partial, Object):
    """
    Represents a voice channel from Discord.

    ---

    This is an event-specific dataclass that is not passed by
    Discord's Gateway. This will only contain the data relevant
    to a voice channel -- and just the `id` of it. `type` is
    dropped as this is already given for the event handler via.
    specification in the typehinting.

    ---

    Attributes
    ----------
    id : `Snowflake`
        The ID of the channel.
    guild_id : `Snowflake`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `Snowflake`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    bitrate : `int`, optional
        The bitrate of the voice channel.
    user_limit : `int`, optional
        The user limit of the voice channel.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `Snowflake`, optional
        The ID of the creator of the group dm or thread.
    application_id : `Snowflake`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `Snowflake`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    rtc_region : `str`, optional
        The channel's voice region ID if present, set to automatic when left as `None`..
    video_quality_mode : `VideoQualityMode`, optional
        The video quality mode of the voice channel.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    id: str | Snowflake = field(converter=Snowflake)
    """The ID of the channel."""
    guild_id: str | Snowflake | None = field(default=None, converter=Snowflake)
    """
    The ID of the guild.

    This is nullable due to some Gateway events
    lacking the data for the ID.
    """
    position: int | None = field(default=None)
    """Sorted position of the channel."""
    permission_overwrites: list[dict] | list[Overwrite] | None = field(default=None)
    """Explicit permission overwrites for members and roles."""
    name: str | None = field(default=None)
    """
    The name of the channel.

    A channel name is in-between 1-100 characters.
    """
    nsfw: bool | None = field(default=False)
    """Whether or not the channel is NSFW. Defaults to `False`."""
    last_message_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """
    The ID of the last message sent in this channel.

    Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    """
    bitrate: int | None = field(default=None)
    """The bitrate of the voice channel."""
    user_limit: int | None = field(default=None)
    """The user limit of the voice channel."""
    rate_limit_per_user: int | None = field(default=None)
    """
    Amount of seconds a user has to wait before sending another message

    Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    """
    icon: str | None = field(default=None)
    """The hash for the channel's icon."""
    owner_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """The ID of the creator of the group dm or thread."""
    application_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """The ID of the application that created the dm if it is bot-created."""
    parent_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """
    The ID of the parent of the channel

    Represents the parent category for regular channels and the parent channel for threads.
    """
    last_pin_timestamp: str | None = field(default=None)
    """The time when the last message was pinned."""
    rtc_region: str | None = field(default=None)
    """The channel's voice region ID if present, set to automatic when left as `None`."""
    video_quality_mode: int | VideoQualityMode | None = field(
        converter=VideoQualityMode, default=None
    )
    """The video quality mode of the voice channel."""
    message_count: int | None = field(default=None)
    """"
    The approximated amount of messages in a thread.

    Stops counting at `50`.
    """
    member_count: int | None = field(default=None)
    """
    The approximated amount of users in a thread.

    Stops counting at `50`.
    """
    # TODO: implement Thread Metadata object.
    thread_metadata: dict | ThreadMetadata | None = field(  # noqa
        converter=ThreadMetadata, default=None  # noqa
    )  # noqa
    """Thread-specific fields not needed by other channels."""
    # TODO: implement Thread Member object.
    member: dict | ThreadMember | None = field(converter=ThreadMember, default=None)  # noqa
    """
    The thread member representation of the user if they have joined the thread.

    This is only included on certain api endpoints.
    """
    default_auto_archive_duration: int | None = field(default=None)
    """
    The default archive duration for threads in minutes.

    Can be set to `60`, `1440`, `4320`, `10080`.
    """
    permissions: str | None = field(default=None)
    """
    The computed permissions for the invoking user in the channel, including any overwrites.

    Only included when part of the resolved data received on a slash command interaction.
    """
    flags: int | ChannelFlags | None = field(converter=ChannelFlags, default=None)
    """Channel flags combined as a bitfield."""


@define(kw_only=True)
class StageChannel(Partial, Object):
    """
    Represents a stage channel from Discord.

    ---

    This is an event-specific dataclass that is not passed by
    Discord's Gateway. This will only contain the data relevant
    to a stage channel -- and just the `id` of it. `type` is
    dropped as this is already given for the event handler via.
    specification in the typehinting.

    ---

    Attributes
    ----------
    id : `Snowflake`
        The ID of the channel.
    guild_id : `Snowflake`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    bitrate : `int`, optional
        The bitrate of the voice channel.
    icon : `str`, optional
        The hash for the channel's icon.
    parent_id : `Snowflake`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    rtc_region : `str`, optional
        The channel's voice region ID if present, set to automatic when left as `None`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    id: str | Snowflake = field(converter=Snowflake)
    """The ID of the channel."""
    type: int | ChannelType = field(converter=ChannelType)
    """The type of the channel."""
    guild_id: str | Snowflake | None = field(default=None, converter=Snowflake)
    """
    The ID of the guild.

    This is nullable due to some Gateway events
    lacking the data for the ID.
    """
    position: int | None = field(default=None)
    """Sorted position of the channel."""
    name: str | None = field(default=None)
    """
    The name of the channel.

    A channel name is in-between 1-100 characters.
    """
    bitrate: int | None = field(default=None)
    """The bitrate of the voice channel."""
    icon: str | None = field(default=None)
    """The hash for the channel's icon."""
    parent_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """
    The ID of the parent of the channel

    Represents the parent category for regular channels and the parent channel for threads.
    """
    permissions: str | None = field(default=None)
    """
    The computed permissions for the invoking user in the channel, including any overwrites.

    Only included when part of the resolved data received on a slash command interaction.
    """
    flags: int | ChannelFlags | None = field(converter=ChannelFlags, default=None)
    """Channel flags combined as a bitfield."""


@define(kw_only=True)
class ThreadChannel(Partial, Object):
    """
    Represents a thread channel from Discord.

    ---

    This is an event-specific dataclass that is not passed by
    Discord's Gateway. This will only contain the data relevant
    to a thread channel -- and just the `id` of it. `type` is
    dropped as this is already given for the event handler via.
    specification in the typehinting.

    ---

    Attributes
    ----------
    id : `Snowflake`
        The ID of the channel.
    guild_id : `Snowflake`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    last_message_id : `Snowflake`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `Snowflake`, optional
        The ID of the creator of the group dm or thread.
    parent_id : `Snowflake`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    id: str | Snowflake = field(converter=Snowflake)
    """The ID of the channel."""
    guild_id: str | Snowflake | None = field(default=None, converter=Snowflake)
    """
    The ID of the guild.

    This is nullable due to some Gateway events
    lacking the data for the ID.
    """
    name: str | None = field(default=None)
    """
    The name of the channel.

    A channel name is in-between 1-100 characters.
    """
    last_message_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """
    The ID of the last message sent in this channel.

    Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    """
    rate_limit_per_user: int | None = field(default=None)
    """
    Amount of seconds a user has to wait before sending another message

    Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    """
    icon: str | None = field(default=None)
    """The hash for the channel's icon."""
    owner_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """The ID of the creator of the group dm or thread."""
    parent_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """
    The ID of the parent of the channel

    Represents the parent category for regular channels and the parent channel for threads.
    """
    """The video quality mode of the voice channel."""
    message_count: int | None = field(default=None)
    """"
    The approximated amount of messages in a thread.

    Stops counting at `50`.
    """
    member_count: int | None = field(default=None)
    """
    The approximated amount of users in a thread.

    Stops counting at `50`.
    """
    # TODO: implement Thread Metadata object.
    thread_metadata: dict | ThreadMetadata | None = field(  # noqa
        converter=ThreadMetadata, default=None  # noqa
    )  # noqa
    """Thread-specific fields not needed by other channels."""
    # TODO: implement Thread Member object.
    member: dict | ThreadMember | None = field(converter=ThreadMember, default=None)  # noqa
    """
    The thread member representation of the user if they have joined the thread.

    This is only included on certain api endpoints.
    """
    default_auto_archive_duration: int | None = field(default=None)
    """
    The default archive duration for threads in minutes.

    Can be set to `60`, `1440`, `4320`, `10080`.
    """
    permissions: str | None = field(default=None)
    """
    The computed permissions for the invoking user in the channel, including any overwrites.

    Only included when part of the resolved data received on a slash command interaction.
    """
    flags: int | ChannelFlags | None = field(converter=ChannelFlags, default=None)
    """Channel flags combined as a bitfield."""


@define()
class Channel(Object):
    """
    Represents a channel from Discord.

    Attributes
    ----------
    id : `Snowflake`
        The ID of the channel.
    type : `ChannelType`
        The type of the channel.
    guild_id : `Snowflake`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    topic : `str`, optional
        The topic of the channel.

        A channel topic is in-between 1-1024 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `Snowflake`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    bitrate : `int`, optional
        The bitrate of the voice channel.
    user_limit : `int`, optional
        The user limit of the voice channel.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    recipients : `list[User]`, optional
        The recipients of the dm.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `Snowflake`, optional
        The ID of the creator of the group dm or thread.
    application_id : `Snowflake`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `Snowflake`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    rtc_region : `str`, optional
        The channel's voice region ID if present, set to automatic when left as `None`..
    video_quality_mode : `VideoQualityMode`, optional
        The video quality mode of the voice channel.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    id: str | Snowflake = field(converter=Snowflake)
    """The ID of the channel."""
    type: int | ChannelType = field(converter=ChannelType)
    """The type of the channel."""
    guild_id: str | Snowflake | None = field(default=None, converter=Snowflake)
    """
    The ID of the guild.

    This is nullable due to some Gateway events
    lacking the data for the ID.
    """
    position: int | None = field(default=None)
    """Sorted position of the channel."""
    permission_overwrites: list[dict] | list[Overwrite] | None = field(default=None)
    """Explicit permission overwrites for members and roles."""
    name: str | None = field(default=None)
    """
    The name of the channel.

    A channel name is in-between 1-100 characters.
    """
    topic: str | None = field(default=None)
    """
    The topic of the channel.

    A channel topic is in-between 1-1024 characters.
    """
    nsfw: bool | None = field(default=False)
    """Whether or not the channel is NSFW. Defaults to `False`."""
    last_message_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """
    The ID of the last message sent in this channel.

    Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    """
    bitrate: int | None = field(default=None)
    """The bitrate of the voice channel."""
    user_limit: int | None = field(default=None)
    """The user limit of the voice channel."""
    rate_limit_per_user: int | None = field(default=None)
    """
    Amount of seconds a user has to wait before sending another message

    Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    """
    recipients: list[dict] | list[User] | None = field(default=None)
    """The recipients of the dm."""
    icon: str | None = field(default=None)
    """The hash for the channel's icon."""
    owner_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """The ID of the creator of the group dm or thread."""
    application_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """The ID of the application that created the dm if it is bot-created."""
    parent_id: str | Snowflake | None = field(converter=Snowflake, default=None)
    """
    The ID of the parent of the channel

    Represents the parent category for regular channels and the parent channel for threads.
    """
    last_pin_timestamp: str | None = field(default=None)
    """The time when the last message was pinned."""
    rtc_region: str | None = field(default=None)
    """The channel's voice region ID if present, set to automatic when left as `None`."""
    video_quality_mode: int | VideoQualityMode | None = field(
        converter=VideoQualityMode, default=None
    )
    """The video quality mode of the voice channel."""
    message_count: int | None = field(default=None)
    """"
    The approximated amount of messages in a thread.

    Stops counting at `50`.
    """
    member_count: int | None = field(default=None)
    """
    The approximated amount of users in a thread.

    Stops counting at `50`.
    """
    # TODO: implement Thread Metadata object.
    thread_metadata: dict | ThreadMetadata | None = field(  # noqa
        converter=ThreadMetadata, default=None  # noqa
    )  # noqa
    """Thread-specific fields not needed by other channels."""
    # TODO: implement Thread Member object.
    member: dict | ThreadMember | None = field(converter=ThreadMember, default=None)  # noqa
    """
    The thread member representation of the user if they have joined the thread.

    This is only included on certain api endpoints.
    """
    default_auto_archive_duration: int | None = field(default=None)
    """
    The default archive duration for threads in minutes.

    Can be set to `60`, `1440`, `4320`, `10080`.
    """
    permissions: str | None = field(default=None)
    """
    The computed permissions for the invoking user in the channel, including any overwrites.

    Only included when part of the resolved data received on a slash command interaction.
    """
    flags: int | ChannelFlags | None = field(converter=ChannelFlags, default=None)
    """Channel flags combined as a bitfield."""
