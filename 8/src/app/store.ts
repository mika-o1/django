import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import { combineReducers } from "redux";
import thunk from "redux-thunk";

import {TodosReducer} from '../pages/Home';

const globalReducer = combineReducers({
  todos: TodosReducer,
});

const initialState = {
};

export const store = configureStore({
  reducer: globalReducer,
  devTools: true,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
  preloadedState: initialState,
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
