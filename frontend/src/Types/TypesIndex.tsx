export type IUser = {
  id: number;
  name: string;
  username: string;
  email: string;
  phone: string;
  website: string;
};

export type IComment = {
  id: number;
  postId: number;
  name: string;
  email: string;
  body: string;
};

export interface IPost {
  id: number;
  userId: number;
  title: string;
  body: string;
  comments?: IComment[];
}

export interface IFallbackProps {
  error: Error;
  resetErrorBoundary: () => void;
}

export interface ICardProps {
  columnClassName?: string;
  cardClassName?: string;
  headerClassName?: string;
  title: string;
  children: React.ReactNode;
}
