export default interface UserData {
  token?: string;
  user?: {
    avatar?: string;
    discord_id?: number;
    permissions?: string[];
    permissions_str?: string;
    username?: string;
    exp?: number;
  };
}
